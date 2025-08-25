from django.contrib import admin
from .models import Student, ParentChild


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(ParentChild)
class ParentChildAdmin(admin.ModelAdmin):
    pass
