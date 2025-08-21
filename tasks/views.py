from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return render(request, "tasks/task_form.html")

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            task.title = title
            task.save()
        return redirect("task_list")
    # 👇 ここを変更
    return render(request, "tasks/edit_task.html", {"task": task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
