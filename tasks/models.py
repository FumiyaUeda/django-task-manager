from django.db import models
from django.core.exceptions import ValidationError

def validate_year(value):
    if value.year < 1900 or value.year > 2100:
        raise ValidationError("期限の年は 1900〜2100 の間で指定してください。")

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("high", "高"),
        ("medium", "中"),
        ("low", "低"),
    ]

    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True, validators=[validate_year])
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
