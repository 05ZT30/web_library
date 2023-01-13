from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

# UserModel: AbstractBaseUser = get_user_model()

class User(models.Model):
    # Manager = 1
    # Teacher = 2
    # Student = 3

    # GROUPS_CHOICES = (
    #     (Manager, "管理员"),
    #     (Teacher, "教师"),
    #     (Student, "学生"),
    # )
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    

    class Meta:
        # permissions = 
        verbose_name = _("用户")
        verbose_name_plural = _("所有用户")
