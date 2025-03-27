from django.shortcuts import render, redirect
from django.contrib import messages
from todoapp.models import Task

def task_list(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to view your tasks")
        return redirect('user_login')  # Redirect to login page
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def create_task(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to create tasks")
        return redirect('user_login')
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date
        )
        messages.success(request, "Task created successfully")
        return redirect('task_list')
        
    return render(request, 'todoapp/create_task.html')

def edit_task(request, task_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to edit tasks")
        return redirect('user_login')
    
    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        messages.error(request, "Task not found")
        return redirect('user_login')
    
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.completed = 'completed' in request.POST
        task.save()
        messages.success(request, "Task updated successfully")
        return redirect('task_list')
        
    return render(request, 'todoapp/edit_task.html', {'task': task})

def delete_task(request, task_id):

    if not request.user.is_authenticated:
        messages.error(request, "Please login to delete tasks")
        return redirect('user_login')

    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        messages.success(request, "Task deleted successfully")
    except Task.DoesNotExist:
        messages.error(request, "Task not found")
    
    return redirect('task_list')


'''
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

def task_list(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to view your tasks")
        return redirect('user_login')  # Make sure 'login_page' is defined in your URLs
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        Task.objects.create(user=request.user, title=title, description=description, due_date=due_date)
        return redirect('task_list')
    return render(request, 'todoapp/create_task.html')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'todoapp/edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

    from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

def task_list(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to view your tasks")
        return redirect('user_login')  # Assuming 'user_login' is your login URL name
    
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, 'todoapp/task_list.html', context)

def create_task(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to create tasks")
        return redirect('user_login')
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        
        if not title:  # Basic validation
            messages.error(request, "Title is required")
            return redirect('create_task')
            
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date if due_date else None
        )
        messages.success(request, "Task created successfully")
        return redirect('task_list')
        
    return render(request, 'todoapp/create_task.html')

def edit_task(request, task_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to edit tasks")
        return redirect('user_login')
    
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.completed = 'completed' in request.POST
        task.save()
        messages.success(request, "Task updated successfully")
        return redirect('task_list')
        
    context = {
        'task': task
    }
    return render(request, 'todoapp/edit_task.html', context)

def delete_task(request, task_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to delete tasks")
        return redirect('user_login')
    
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect('task_list')
        
    context = {
        'task': task
    }
    return render(request, 'todoapp/delete_task.html', context)
'''

