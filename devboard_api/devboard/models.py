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
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TaskNote(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    resources = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    date_worked = models.DateField(default='2021-01-01')
    time_worked = models.IntegerField(default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description