import logging

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from .models import Task

from .forms import TaskForm
logger = logging.getLogger(__name__)


def index(request):
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            logger.info("Created task: %s", form)
            form.save()
        return redirect('/')

    context = {"tasks": tasks, "TaskForm": form}
    return render(request, 'tasks.html', context)


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        logger.info("Updated task: %s", task)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, 'update_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        logger.info("Removing task: %s", task)
        task.delete()
        return redirect("/")

    context = {"task": task}
    return render(request, 'delete_task.html', context)

