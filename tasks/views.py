from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Task
from .forms import TaskForm

# タスク一覧（検索・ソート・完了フィルタ対応）
def task_list(request):
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "deadline")

    tasks = Task.objects.all()

    # 🔍 検索（タイトル・詳細に含まれる文字列）
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(detail__icontains=query))

    # 並び替えマップ
    sort_map = {
        "deadline": ["deadline"],             # 期限が近い順
        "deadline_desc": ["-deadline"],       # 期限が遠い順
        "title": ["title"],                   # タイトル順
        "priority": ["priority", "-created_at"],  # 優先度順（同じなら新しい順）
    }
    tasks = tasks.order_by(*sort_map.get(sort, ["deadline"]))

    context = {
        "tasks": tasks,
        "query": query,
        "sort": sort,
    }
    return render(request, "tasks/task_list.html", context)


# タスク作成
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
    return render(request, "tasks/task_form.html", {"form": form})


# タスク削除
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return redirect("task_list")


# 完了状態のトグル
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_completed = not task.is_completed
        task.save()
    return redirect("task_list")
