from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from app.mixins import SecondMixin


# Create your views here.
class ListView(SecondMixin):
    template_name = 'index.html'

def registration(request):
    return render(request, 'registration.html')


class SignUp(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')

        return super().get(request, *args, **kwargs)


class LoginForm(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('index')

def user_logout(request):
    logout(request)
    return redirect('index')