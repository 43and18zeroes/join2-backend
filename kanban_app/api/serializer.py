from rest_framework import serializers
from kanban_app.models import User, Task, Subtask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type', 'initials']
        extra_kwargs = {
            'email': {'required': False}
        }

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'is_completed']

class TaskReadSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    subtasks = SubtaskSerializer(many=True, read_only=True)
    category_choices = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'category', 'due_date', 'priority', 
            'users', 'status', 'position', 'subtasks', 'category_choices'
        ]
    
    def get_category_choices(self, obj):
        return Task.CATEGORY_CHOICES

class TaskWriteSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    subtasks = SubtaskSerializer(many=True)
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'category', 'due_date', 'priority', 
            'users', 'status', 'position', 'subtasks'
        ]
    
    def create(self, validated_data):
        print("Validated data received in serializer:", validated_data)
        users_data = validated_data.pop('users')
        subtasks_data = validated_data.pop('subtasks')
        task = Task.objects.create(**validated_data)
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(**user_data)
            task.users.add(user)
        
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        
        return task

    def update(self, instance, validated_data):
        users_data = validated_data.pop('users', None)
        subtasks_data = validated_data.pop('subtasks', None)
        instance = super().update(instance, validated_data)
        
        if users_data:
            instance.users.clear()
            for user_data in users_data:
                user, created = User.objects.get_or_create(**user_data)
                instance.users.add(user)
        
        if subtasks_data:
            instance.subtasks.all().delete()
            for subtask_data in subtasks_data:
                Subtask.objects.create(task=instance, **subtask_data)
        
        return instance