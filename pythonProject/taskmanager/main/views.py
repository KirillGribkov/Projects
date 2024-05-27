from django.shortcuts import render

import numpy as np
import torch
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from .forms import *
from .models import Task
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('main:login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'main/registr.html', {"form": form})


def login(request):
    return render(request, 'main/login.html')


def index(request):

    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def about(request):
    return render(request, 'main/about.html')





@csrf_protect
def login(request):
    data = {}

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'main/index.html')
        else:
            data['login_error'] = "Проверьте правилность данных"
            return render(request, 'main/login.html', data)
    else:
        return render(request, 'main/login.html', data)

@csrf_protect
@login_required(login_url='/')
def profile(request):
    username = auth.get_user(request).username
    user = User.objects.get(username=username)
    if request.method == 'POST':

        form = Works(request.POST)
        Text = request.POST.get('input1', '')
        Choise = request.POST.get('input2', '')
        np.random.seed(42)
        torch.manual_seed(42)
        if Choise == "Leskov":
            model_name_or_path = "C:\\Pycharm\\pythonProject\\taskmanager\\main\\models\\L"
            tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
            model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()
            text = Text
            input_ids = tokenizer.encode(text, return_tensors="pt").cpu()
            out = model.generate(input_ids.cpu())
            generated_text = list(map(tokenizer.decode, out))[0]
            Text = generated_text
            return render(request, 'main/profile.html', {'user': user, 'form': form, 'Text': Text})
        if Choise == "Tolstoy":
            model_name_or_path = "C:\\Pycharm\\pythonProject\\taskmanager\\main\\models\\T"
            tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
            model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()
            text = Text
            input_ids = tokenizer.encode(text, return_tensors="pt").cpu()
            out = model.generate(input_ids.cpu())
            generated_text = list(map(tokenizer.decode, out))[0]
            Text = generated_text
            return render(request, 'main/profile.html', {'user': user, 'form': form, 'Text': Text})
        if Choise == "Sber":
            model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
            tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
            model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()
            text = Text
            input_ids = tokenizer.encode(text, return_tensors="pt").cpu()
            out = model.generate(input_ids.cpu())
            generated_text = list(map(tokenizer.decode, out))[0]
            Text = generated_text
            return render(request, 'main/profile.html', {'user': user, 'form': form, 'Text': Text})

    else:
        Text = ""
        form = Works()
    return render(request, 'main/profile.html', {'user': user, 'form': form, 'Text': Text})


def logout(request):
    auth.logout(request)
    return render(request, 'main/login.html')



