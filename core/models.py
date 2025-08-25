from django.db import models

class Grade(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Session(models.Model):
    session_year = models.CharField(max_length=15, unique=True)
    term = models.CharField(max_length=10, choices=[
        ('1', 'First Term'),
        ('2', 'Second Term'),
        ('3', 'Third Term'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.term} term, {self.session_year} session'
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name