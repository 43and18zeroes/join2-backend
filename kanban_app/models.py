from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    dueDate = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    assignedTo = models.CharField(max_length=255)
    subTasks = models.CharField(max_length=255)
    subTasksCompleted = models.JSONField()
    taskStatus = models.CharField(max_length=255)
    taskColumnOrder = models.IntegerField()
    firebaseId = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

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
        return self.name