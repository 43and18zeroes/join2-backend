# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user.username

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(
    max_length=15,
    null=True,
    blank=True,
    help_text="Telephone number in the format: '999999999'. Up to 15 digits allowed."
    )
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
        if self.first_name and self.last_name:
            self.initials = f"{self.first_name[0]}{self.last_name[0]}".upper()
        super().save(*args, **kwargs)