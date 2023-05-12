from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from uuid import uuid4

# Create your models here.
class User(models.Model):
    """User Model"""
    # userid = models.CharField(max_length=50, default=lambda: str(uuid4), unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=255, null=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'city']

    def __str__(self) -> str:
        return self.email

