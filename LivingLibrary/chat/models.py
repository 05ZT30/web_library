from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

UserModel: AbstractBaseUser = get_user_model()