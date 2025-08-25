from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Parent(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='parent')
    can_check_result = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, unique=True, validators=[
                             RegexValidator(r'^\d{11}$')], null=True, blank=True)
    

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.phone_number