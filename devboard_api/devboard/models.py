from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    due_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TaskNote(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    resources = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description