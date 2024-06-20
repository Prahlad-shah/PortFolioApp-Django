from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserModel, AuthenticationForm
from django.contrib.auth.forms import UserModel
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def indexPage(request):
    return render(request, 'AuthPages/landingpage.html')

class UserSignUpView(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'registration/create_account.html'
    success_url = 'login'

    

    

