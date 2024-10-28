from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskSerializer
from kanban_app.models import Task

@api_view(['GET', 'POST'])
def first_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)