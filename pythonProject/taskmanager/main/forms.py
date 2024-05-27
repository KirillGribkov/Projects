from .models import Task
from django.forms import ModelForm, TextInput, DateInput, Textarea, FileInput
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Works(forms.Form):
    AVTOR = (
        ("Leskov", "Лесков"),
        ("Tolstoy", "Толстой"),
        ("Sber", "Сбер"))
    input1 = forms.CharField(label="Ваш текст",widget=forms.Textarea(attrs={'cols':60, 'rows': 10}))
    input2 = forms.ChoiceField(label="Автор", choices=AVTOR)


