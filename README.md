\# Django Task Manager



Djangoで作成したシンプルなタスク管理アプリです。  

タスクの追加・編集・削除が可能なCRUD機能を実装しています。



\## 機能

\- タスク一覧表示

\- タスク新規作成

\- タスク編集

\- タスク削除

\- Django管理画面からの操作



\## 技術スタック

\- Python 3.11

\- Django 5.2

\- SQLite（開発環境）

\- Bootstrap（UI調整予定）



\## 動作方法

```bash

git clone https://github.com/FumiyaUeda/django-task-manager.git

cd django-task-manager

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver



