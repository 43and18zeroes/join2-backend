from rest_framework import serializers
from kanban_app.models import User, Task, Subtask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_color', 'type']

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'is_completed', 'task']

class TaskSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)  # Nested representation of users
    subtasks = SubtaskSerializer(many=True, read_only=True)  # Nested subtasks
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'category', 'due_date', 'priority', 
            'users', 'status', 'position', 'subtasks'
        ]
    
    def create(self, validated_data):
        users_data = validated_data.pop('users')
        task = Task.objects.create(**validated_data)
        for user_data in users_data:
            user, created = User.objects.get_or_create(**user_data)
            task.users.add(user)
        return task

    def update(self, instance, validated_data):
        users_data = validated_data.pop('users', None)
        if users_data:
            instance.users.clear()
            for user_data in users_data:
                user, created = User.objects.get_or_create(**user_data)
                instance.users.add(user)
        
        return super().update(instance, validated_data)
