from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django_enum import EnumField
from uuid import uuid4

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, city="Lagos", country="Nigeria"):
        """ creates and saves a User
        """
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            city=city,
            country=country,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser):
    """User Model"""
    userid = models.CharField(max_length=50, default=str(uuid4()))
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=255, null=False, default="Lagos")
    country = models.CharField(max_length=255, null=False, default="Nigeria")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userid','password', 'city', 'country']
    objects = UserManager()

    def __str__(self) -> str:
        return self.userid + ' ' + self.email

