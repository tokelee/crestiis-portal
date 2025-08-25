from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUserManager(UserManager):
    def _create_user(self, login_id, password, **extra_fields):
        # if not login_id:
        #     raise ValueError("The login ID must be set")
        user = CustomUser(login_id=login_id, **extra_fields)
        if password:
            user.password = make_password(password)
        try:
            user.save(using=self._db)
            return user
        except Exception as e:
            raise e
    
    def create_user(self, login_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login_id, password, **extra_fields)
    
    def create_superuser(self, login_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(login_id, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    last_name = models.CharField(blank=False, max_length=80)
    first_name = models.CharField(blank=False, max_length=80)
    middle_name = models.CharField(null=True, blank=True, max_length=80)
    email = models.EmailField(max_length=191, unique=True)
    login_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length=80, choices=[
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent'),
        ('ADMIN', 'Admin')
    ])

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.login_id
