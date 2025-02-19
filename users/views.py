from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm


# from users.forms import UserForm

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'users/register.html'
#     extra_context = {'title': "Регистрация"}


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm
    return render(request, 'users/register.html', {'form': form})