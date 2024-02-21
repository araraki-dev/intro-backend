from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def todo_lists(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists})

def todo_list_detail(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, pk=todo_list_id)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list})

def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-lists')
    else:
        form = TodoListForm()
    return render(request, 'todos/create_todo_list.html', {'form': form})

def delete_todo_list(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, pk=todo_list_id)
    if request.method == 'POST':
        todo_list.delete()
        return redirect('todo-lists')
    return render(request, 'todos/delete_todo_list.html', {'todo_list': todo_list})

def edit_todo_list(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, pk=todo_list_id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todos/todo-list-detail', todo_list_id=todo_list.id)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/edit_todo_list.html', {'form': form})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo-list-detail', todo_list_id=todo.todo_list.id)
    return render(request, 'todos/delete_todo.html', {'todo': todo})

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-list-detail', todo_list_id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form})
