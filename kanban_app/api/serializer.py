from rest_framework import serializers
from kanban_app.models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100)
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)