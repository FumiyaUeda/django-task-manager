from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "is_completed"]
        labels = {
            "title": "タイトル",
            "description": "詳細",
            "due_date": "期限",
            "is_completed": "完了",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "例）会議、買い物、締切など"}),
            "description": forms.Textarea(attrs={"placeholder": "詳細を入力"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
