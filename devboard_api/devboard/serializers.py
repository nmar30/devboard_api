from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task, TaskNote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',  'first_name', 'last_name')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members']


class ProjectNestedSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'status', 'due_date', 'owner']


class TaskNestedSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'status', 'due_date', 'owner']


class TaskNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskNote
        fields = ['id', 'task', 'description', 'resources', 'start_time', 'end_time', 'owner']


class TaskNoteNestedSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = TaskNote
        fields = ['id', 'task', 'description', 'resources', 'start_time', 'end_time', 'owner']