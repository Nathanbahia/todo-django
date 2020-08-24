from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TaskModel
from .forms import TaskModelForm


def index(request):
    tasks = TaskModel.objects.filter(active=True)
    form = TaskModelForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
           form.save()
           form = TaskModelForm()
           messages.success(request, 'Task save successfuly')
        else:
            messages.error(request, 'Error')
    return render(request, 'index.html', {'form': form, 'tasks': tasks})


def remove(request, id):
    task = TaskModel.objects.get(pk=id)
    task.active = False
    task.save()
    return redirect(index)

def edit(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskModelForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            task = TaskModel.objects.get(pk=id)
            task.text = form.cleaned_data['text']
            task.save()
            return redirect(index)
    return render(request, 'edit.html', {'form': form, 'task': task})
