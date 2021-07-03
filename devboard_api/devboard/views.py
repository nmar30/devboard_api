from django.shortcuts import render
from .models import Project, Task, TaskNote
from .serializers import ProjectSerializer, TaskSerializer, TaskNoteSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ProjectList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        try:
            return Project.objects.filter(members=user_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request):
        user_id = self.request.query_params.get('user')
        project = self.get_object(user_id)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project)
        project.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class TaskList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, project_id):
        try:
            return Task.objects.filter(project=project_id)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, project_id):
        tasks = self.get_object(project_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, project_id):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, project_id, task_id):
        try:
            return Task.objects.get(project=project_id, pk=task_id)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, project_id, task_id):
        task = self.get_object(project_id, task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, project_id, task_id):
        task = self.get_object(project_id, task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, task_id):
        task = self.get_object(project_id, task_id)
        serializer = TaskSerializer(task)
        task.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class TaskNoteList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, project_id, task_id):
        try:
            return TaskNote.objects.filter(task=task_id)
        except TaskNote.DoesNotExist:
            raise Http404

    def get(self, request, project_id, task_id):
        tasknotes = self.get_object(project_id, task_id)
        serializer = TaskNoteSerializer(tasknotes, many=True)
        return Response(serializer.data)

    def post(self, request, project_id, task_id):
        serializer = TaskNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskNoteDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, task_id, note_id):
        try:
            return TaskNote.objects.get(task=task_id, pk=note_id)
        except TaskNote.DoesNotExist:
            raise Http404

    def get(self, request, project_id, task_id, note_id):
        task_note = self.get_object(task_id, note_id)
        serializer = TaskNoteSerializer(task_note)
        return Response(serializer.data)

    def put(self, request, project_id, task_id, note_id):
        task_note = self.get_object(task_id, note_id)
        serializer = TaskNoteSerializer(task_note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, task_id, note_id):
        task_note = self.get_object(task_id, note_id)
        serializer = TaskNoteSerializer(task_note)
        task_note.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)