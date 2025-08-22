from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# タスク削除（一覧のみから実行）
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    # GET では確認画面を出さず一覧へ戻す
    return redirect("task_list")

# タスク一覧
def task_list(request):
    tasks = Task.objects.all().order_by("-deadline")  # created_at → deadline に修正
    return render(request, "tasks/task_list.html", {"tasks": tasks})

# 新規作成
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "is_update": False})

# 編集
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "task": task, "is_update": True})

# 完了切り替え
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_completed = not task.is_completed
        task.save()
    return redirect("task_list")
