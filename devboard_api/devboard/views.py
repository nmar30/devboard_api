from django.shortcuts import render
from .models import Project, Task, TaskNote
from .serializers import ProjectSerializer, TaskSerializer, TaskNoteSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

# Create your views here.
class ProjectList(APIView):
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)