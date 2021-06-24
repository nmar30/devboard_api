from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:project_id>', views.ProjectDetails.as_view()),
    path('projects/<int:project_id>/tasks/', views.TaskList.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>', views.TaskDetails.as_view()),
]