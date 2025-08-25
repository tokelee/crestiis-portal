from django.contrib import admin
from .models import Grade, Session, Subject


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass