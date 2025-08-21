# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ルート直下（/）でタスクアプリを表示
    path('', include('tasks.urls')),

    # 互換のため /tasks/ パスでも同じものを見られるようにする
    path('tasks/', include('tasks.urls')),
]
