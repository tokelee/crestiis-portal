from django.contrib import admin
from .models import Result, Score


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass