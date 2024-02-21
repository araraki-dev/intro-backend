from django.shortcuts import render, get_object_or_404, redirect
from .forms import TodoForm
from .models import Todo

def todo_list(request):
    Todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'Todos': Todos})

def todo_detail(request, id):
    Todo = get_object_or_404(Todo, pk=id)
    return render(request, 'todos/todo_detail.html', {'Todo': Todo})

def todo_delete(request, id):
    Todo = get_object_or_404(Todo, pk=id)
    Todo.delete()
    return redirect('todo_list')

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})
