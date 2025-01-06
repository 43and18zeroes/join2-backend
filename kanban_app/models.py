from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from user_auth_app.models import UserProfile

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Due date must be in the future.")
due_date = models.DateField(validators=[validate_future_date])

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    CATEGORY_CHOICES = [
        ('Technical Task', 'Technical Task'),
        ('User Story', 'User Story'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    due_date = models.DateField()
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('urgent', 'Urgent'),
    ]
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    users = models.ManyToManyField(UserProfile, related_name='tasks')
    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('in_progress', 'In progress'),
        ('await_feedback', 'Await feedback'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    position = models.IntegerField()
    
    def __str__(self):
        return self.title

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Subtask of {self.task.title})"