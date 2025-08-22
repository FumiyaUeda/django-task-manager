from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Q


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
    query = request.GET.get("q", "")
    sort = request.GET.get("sort", "deadline")  # デフォルトは期限昇順

    tasks = Task.objects.all()

    # 🔍 検索（タイトル or 詳細に含まれるもの）
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) | Q(detail__icontains=query)
        )

    # 🔽 ソート処理
    if sort == "deadline":
        tasks = tasks.order_by("deadline")  # 期限が近い順
    elif sort == "deadline_desc":
        tasks = tasks.order_by("-deadline")  # 期限が遠い順
    elif sort == "title":
        tasks = tasks.order_by("title")  # タイトル順
    else:
        tasks = tasks.order_by("deadline")  # フォールバック

    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "query": query,
        "sort": sort,
    })


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
