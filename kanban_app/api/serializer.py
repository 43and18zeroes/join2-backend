from rest_framework import serializers
from kanban_app.models import Task

class TaskSerializer(serializers.Serializer):  
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    category = serializers.CharField(max_length=255)
    dueDate = serializers.CharField(max_length=255)
    priority = serializers.CharField(max_length=255)
    assignedTo = serializers.CharField(max_length=255)
    subTasks = serializers.CharField(max_length=255)
    subTasksCompleted = serializers.CharField(max_length=255)
    taskStatus = serializers.CharField(max_length=255)
    taskColumnOrder = serializers.CharField(max_length=255)
    firebaseId = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)