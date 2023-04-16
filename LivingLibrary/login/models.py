from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, card_id, username, password, email):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            card_id=card_id,
            username=username,
            password=password,
            email=self.normalize_email(email),
            # date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, card_id, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            card_id=card_id,
            username=username,
            password=password,
            # date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_teacher(self, card_id, username, password, catagory):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            card_id=card_id,
            username=username,
            password=password,
            catagory=catagory,
            # email=self.normalize_email(email),
            # date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    card_id = models.CharField(max_length=6, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['card_id', 'password', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        # permissions =
        verbose_name = "用户"
        verbose_name_plural = "所有用户"


class MyTeacher(AbstractBaseUser):
    card_id = models.CharField(max_length=6, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )
    phone = models.CharField(max_length=11)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    catagory = models.CharField(max_length=20)
    photo = models.ImageField(null=True)
    introduction = models.TextField(null= True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['card_id', 'password', 'catagory']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        # permissions =
        verbose_name = "教师"
        verbose_name_plural = "所有教师"
