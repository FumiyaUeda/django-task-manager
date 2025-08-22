# Django Task Manager

Djangoで作成したシンプルなタスク管理アプリです。  
タスクの追加・編集・削除・完了状態の切替・期限設定が可能です。  
就職活動用ポートフォリオとして、Heroku上にもデプロイしています。

---

## 機能

- タスク一覧表示
  - 完了タスクは色分け表示
  - 期限を表示
- タスク新規作成
  - タイトル・詳細・期限を入力
  - 年号は4桁必須
- タスク編集
- タスク削除（確認なし即時削除）
- タスク完了／未完了の切替（チェックボックス）
- Django管理画面からの操作

---

## 技術スタック

- Python 3.11
- Django 5.2
- SQLite（開発環境）
- PostgreSQL（本番環境 / Heroku）
- Bootstrap 5（UI）

---

## デモ

- Heroku デプロイ先: [https://django-task-manager-fumiya.herokuapp.com](https://django-task-manager-fumiya.herokuapp.com)  
  （※起動に数秒かかる場合があります）

---

## セットアップ方法（ローカル環境）

```bash
# リポジトリをクローン
git clone https://github.com/FumiyaUeda/django-task-manager.git
cd django-task-manager

# 仮想環境を作成して有効化
python -m venv venv
.\venv\Scripts\activate   # Windowsの場合
# source venv/bin/activate # macOS/Linuxの場合

# 依存パッケージをインストール
pip install -r requirements.txt

# マイグレーション & 開発サーバー起動
python manage.py migrate
python manage.py runserver
