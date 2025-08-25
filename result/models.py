from django.db import models
from core.models import Session, Subject
from student.models import Student

class Result(models.Model):
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Score(models.Model):
    half_term_score = models.IntegerField()
    continous_assessment_score = models.IntegerField()
    exam_score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)