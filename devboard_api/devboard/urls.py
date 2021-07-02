from django.urls import path
from . import views

urlpatterns = [
    path('projects/<int:user_id>', views.ProjectList.as_view()),
    path('projects/<int:project_id>', views.ProjectDetails.as_view()),
    path('projects/<int:project_id>/tasks/', views.TaskList.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>', views.TaskDetails.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>/notes/', views.TaskNoteList.as_view()),
    path('projects/<int:project_id>/tasks/<int:task_id>/notes/<int:note_id>', views.TaskNoteDetails.as_view()),
]