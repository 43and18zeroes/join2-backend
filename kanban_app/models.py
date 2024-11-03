from django.db import models

class User(models.Model):
    userSurName = models.CharField(max_length=255)
    userFirstName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    userEmailAddress = models.CharField(max_length=255)
    userInitials = models.CharField(max_length=255)
    userPhoneNumber = models.CharField(max_length=255)
    userColor = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    firebaseId = models.CharField(max_length=255)
    
    def __str__(self):
        return self.userName

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    CATEGORY_CHOICES = [
        ('technical_task', 'Technical Task'),
        ('user_story', 'User Story'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    due_date = models.DateField()
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('urgent', 'Urgent'),
    ]
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    users = models.ManyToManyField('User', related_name='tasks')
    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('in_progress', 'In progress'),
        ('await_feedback', 'Await feedback'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    taskColumnOrder = models.IntegerField()
    firebaseId = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Subtask of {self.task.title})"