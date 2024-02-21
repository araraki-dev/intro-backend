from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_lists, name='todo-lists'),
    path('create/', views.create_todo_list, name='create-todo-list'),
    path('<int:todo_list_id>/', views.todo_list_detail, name='todo-list-detail'),
    path('<int:todo_list_id>/delete/', views.delete_todo_list, name='delete-todo-list'),
    path('<int:todo_list_id>/edit/', views.edit_todo_list, name='edit-todo-list'),
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='delete-todo'),
    path('todos/<int:todo_id>/edit/', views.edit_todo, name='edit-todo'),
]