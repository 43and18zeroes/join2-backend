from rest_framework import viewsets
from kanban_app.models import User, Task, Subtask
from .serializer import UserSerializer, TaskWriteSerializer, TaskReadSerializer, SubtaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from kanban_app.models import Task

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskWriteSerializer
        return TaskReadSerializer
    
    @action(detail=False, methods=['post'])
    def update_positions(self, request):
        updates = request.data
        if not isinstance(updates, list):
            return Response(
                {"error": "Payload must be a list of {id, position, status} objects."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for update in updates:
            try:
                task = Task.objects.get(id=update.get('id'))
                task.position = update.get('position')
                task.status = update.get('status')
                task.save()
            except Task.DoesNotExist:
                return Response(
                    {"error": f"Task with ID {update.get('id')} not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return Response({"success": "Tasks updated successfully."}, status=status.HTTP_200_OK)

class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
