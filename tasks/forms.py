from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "detail", "deadline", "is_completed"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "detail": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "min": "1900-01-01",
                    "max": "2100-12-31",   # 入力範囲制限を追加
                },
                format="%Y-%m-%d"
            ),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    # 年号は必ず4桁
    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline:
            year = deadline.year
            if len(str(year)) != 4:
                raise forms.ValidationError("年号は4桁で入力してください (例: 2025-08-22)。")
        return deadline
