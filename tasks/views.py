from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm

# タスク一覧
def task_list(request):
    # 未完 → 完了の順に表示（新しい順）
    tasks = Task.objects.all().order_by("is_completed", "-id")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


# タスク新規作成
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


# タスク編集
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    # ← ここで edit_task.html を呼び出すよう統一
    return render(request, "tasks/edit_task.html", {"form": form, "task": task})


# タスク削除
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


# 完了/未完トグル
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_completed = not task.is_completed
        task.save()
    return redirect("task_list")
