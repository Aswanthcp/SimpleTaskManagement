from django.urls import path
from . import views
from .api import task_list,task_detail

app_name = "app"


urlpatterns = [
    path("tasks/", views.taskView, name="taskView"),
    path('tasks/add/', views.create_task_modal, name='create_task_modal'),
    path('update_completed/<int:task_id>/', views.update_completed, name='update_completed'),
    
    
    # rest framework urls 
    path('api/tasks/', task_list, name='task-list'),
    path('api/tasks/<int:pk>/', task_detail, name='task-detail'),
    
]
