
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/members/', ViewTaskMembersView.as_view(), name='view-task-members'),
    path('tasks/<int:pk>/members/add/', AddRemoveTaskMemberView.as_view(), name='add-task-member'),
    path('tasks/<int:pk>/members/remove/', AddRemoveTaskMemberView.as_view(), name='remove-task-member'),
    path('tasks/<int:task_pk>/comments/', CommentListCreateView.as_view(), name='task-comments'),
    path('tasks/<int:pk>/status/', UpdateTaskStatusView.as_view(), name='update-task-status'),
]
   

