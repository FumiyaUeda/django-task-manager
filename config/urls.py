from django.contrib import admin
from django.urls import path
from tasks.views import task_list, task_create, task_edit, task_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", task_list, name="task_list"),
    path("tasks/new/", task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", task_edit, name="task_edit"),
    path("tasks/<int:pk>/delete/", task_delete, name="task_delete"),
]
