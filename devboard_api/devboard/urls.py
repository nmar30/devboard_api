from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:project_id>/', views.ProjectDetails.as_view()),
    path('projects/<int:project_id>/tasks/', views.TaskList.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetails.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>/notes/', views.TaskNoteList.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>/notes/<int:note_id>/', views.TaskNoteDetails.as_view()),
    path('users/', views.UserDetails.as_view()),
    path('data/tasks/', views.UserTaskOwnerList.as_view()),
    path('data/projects/', views.UserProjectOwnerList.as_view()),
]