from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    RoleChoices = [
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('volunteer', 'Volunteer'),
    ]
    role = models.CharField(max_length=20, choices=RoleChoices)
    USERNAME_FIELD = 'email'        
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email