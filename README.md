# Django Task Manager

Djangoで作成したシンプルなタスク管理アプリです。  
タスクの追加・編集・削除・完了状態の切替・期限設定に加え、検索・ソート・優先度管理に対応しています。  
就職活動用ポートフォリオとして、Heroku上にもデプロイしています。

---

## 機能

- タスク一覧表示
  - タイトル・詳細・期限・優先度を表示
  - 完了タスクは色分け表示（背景緑）
- タスク新規作成
  - タイトル・詳細・期限（年号は4桁必須）・優先度を入力
- タスク編集
- タスク削除（確認なし即時削除）
- タスク完了／未完了の切替（チェックボックス）
- 検索（タイトル・詳細を部分一致）
- ソート機能
  - 期限が近い順 / 遠い順
  - タイトル順
  - 優先度順
- Django管理画面からの操作

※「期限の近さで色が変わる」機能は実装途中で削除

---

## 技術スタック

- Python 3.11
- Django 5.2
- SQLite（開発環境）
- PostgreSQL（本番環境 / Heroku）
- Bootstrap 5（UI）

---

## スクリーンショット

### タスク一覧
![タスク一覧](docs/screenshot_list.png)

### タスク作成
![タスク作成](docs/screenshot_add.png)

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
