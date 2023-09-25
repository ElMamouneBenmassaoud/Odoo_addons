from django.db import models

class Developer(models.Model):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)

    def is_free(self):
        return self.tasks.count() == 0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(Developer, related_name="tasks", on_delete=models.CASCADE, null=True, verbose_name="assignee")

    def __str__(self):
        return f"{self.title} ({self.description})"