from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskSerializer
from kanban_app.models import Task
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TaskViewSet(viewsets.ViewSet):
#     queryset = Task.objects.all()
    
#     def list(self, request):
#         serializer = TaskSerializer(self.queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         task = get_object_or_404(self.query, pk=pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = TaskSerializer(self.queryset, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     def destroy(self, request, pk=None):
#         task = get_object_or_404(self.queryset, pk=pk)
#         serializer = TaskSerializer(task)
#         task.delete
#         return Response(serializer.data)

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