from django.db import models
from django.conf import settings
from core.models import Grade
from parent.models import Parent

class Student(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    can_check_result = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    gender = models.CharField(null=True, blank=True, max_length=20, choices=[
        ("MALE", 'Male'),
        ("FEMALE", 'Female')
    ])
    dob = models.DateField(null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return f'{self.account.first_name} - {self.grade}'
    
class ParentChild(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_primary_contact = models.BooleanField(default=False)
    relationship = models.CharField(null=True, blank=True, max_length=20, choices=[
        ("MOTHER", 'Mother'),
        ("FATHER", 'Father'),
        ("GUARDIAN", 'Guardian')
    ])

