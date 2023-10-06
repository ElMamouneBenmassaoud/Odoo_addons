from django.contrib import admin

from developer.models import Developer
from task.models import Task


# Register your models here.

class TaskLine(admin.TabularInline):
    model = Task
    extra = 1


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_free')
    inlines = [TaskLine]


admin.site.register(Developer, DeveloperAdmin)
