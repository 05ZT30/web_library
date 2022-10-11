from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.contrib.auth import get_user_model
# Create your models here.

UserModel: AbstractBaseUser = get_user_model()

# vip = Permission.objects.filter(codename='vip_myuser')
# vip = Permission.objects.filter(codename='vip_myuser')[0]

# class Student(UserModel):
#     group = Group.objects.get(name='groupname')
#     user.groups.add(group)