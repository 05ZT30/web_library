from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.

# UserModel: AbstractBaseUser = get_user_model()


class Person(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)