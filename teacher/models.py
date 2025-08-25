from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from core.models import Grade

class Teacher(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher')
    can_check_result = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    gender = models.CharField(null=True, blank=True, max_length=20, choices=[
        ("MALE", 'Male'),
        ("FEMALE", 'Female')
    ])
    phone_number = models.CharField(max_length=11, unique=True, validators=[
                             RegexValidator(r'^\d{11}$')], null=True, blank=True)
    homeroom = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return f'Grade-{self.grade.name} Homeroom teacher'