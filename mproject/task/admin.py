from django.contrib import admin
from task.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','assignee')
    fields = ['title', 'description', 'assignee']

