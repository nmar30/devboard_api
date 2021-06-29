from rest_framework import serializers
from .models import Project, Task, TaskNote


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members']


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'status', 'due_date', 'owner']


class TaskNoteSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)

    class Meta:
        model = TaskNote
        fields = ['id', 'task', 'description', 'resources', 'start_time', 'end_time', 'owner']