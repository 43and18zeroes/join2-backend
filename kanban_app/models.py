from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    assigned_to = models.CharField(max_length=255)
    sub_tasks = models.CharField(max_length=255)
    sub_tasks_completed = models.CharField(max_length=255)
    task_status = models.CharField(max_length=255)
    task_column_order = models.CharField(max_length=255)
    firebase_id = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class User(models.Model):
    surname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    initials = models.CharField(max_length=255)
    phone_numer = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    firebase_id = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name