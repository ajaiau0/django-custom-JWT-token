from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """
    User Profile Details
    """
    USER_ROLE = (
        ('AD', 'Admin'),
        ('USR', 'User'),
    )

    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE, primary_key=True)
    employeeRole = models.CharField(max_length=6, choices=USER_ROLE)