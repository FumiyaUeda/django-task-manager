from django.db import models
from django.core.exceptions import ValidationError

# 年4桁チェック関数
def validate_year(value):
    if value.year < 1000 or value.year > 9999:
        raise ValidationError("年は4桁で入力してください")

class Task(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)
    deadline = models.DateField(
        blank=True,
        null=True,
        validators=[validate_year],  # ✅ バリデーション追加
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
