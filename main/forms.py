from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm (ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "description"]
        widgets ={"title": TextInput(attrs={'class':'form-contol', 'placeholder': 'Введите название'}),
            "task": Textarea(attrs={'class':'form-contol', 'placeholder': 'Введите описание'}),
            "description": TextInput(attrs={'class':'form-contol', 'placeholder': 'Добавьте комментарий'}),

            }