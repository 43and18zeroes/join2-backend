from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Due date must be in the future.")
due_date = models.DateField(validators=[validate_future_date])


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        help_text="Telephone number in the format: '999999999'. Up to 15 digits allowed."
    )
    # phone_number = models.CharField(
    #     max_length=15,
    #     validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
    #     help_text="Telephone number in the format: '+999999999'. Up to 15 digits allowed."
    # )
    user_color = models.CharField(max_length=7)
    TYPE_CHOICES = [
        ('user_from_signup', 'User from signup'),
        ('user_from_contacts', 'User from contacts'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    initials = models.CharField(max_length=2, blank=True, editable=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Calculate initials from first_name and last_name
        if self.first_name and self.last_name:
            self.initials = f"{self.first_name[0]}{self.last_name[0]}".upper()
        super().save(*args, **kwargs)

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
    users = models.ManyToManyField('User', related_name='tasks')
    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('in_progress', 'In progress'),
        ('await_feedback', 'Await feedback'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    position = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Subtask of {self.task.title})"