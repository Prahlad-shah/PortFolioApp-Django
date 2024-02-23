from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, FormView, ListView, DeleteView, UpdateView
from django.http import HttpResponse
from . import forms
from . import models
# from django.
# Create your views here.

# def indexPage(request):
#     return render(request, 'PortMainPages/homepage.html')
class PortFolioView(TemplateView):
    template_name = 'PortMainPages/homepage.html'
    extra_context = {
                    'user':{'Name':'Prahlad Shah', 'Address': 'Kathmandu'},}
    

class TestView(FormView):
    template_name = 'testpages/indexform.html'
    success_url = '/portfolio'
    model = models.UserModel
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    form_class = forms.RegisterUser
    
    def form_valid(self, form: forms.RegisterUser) -> HttpResponse:
        form.save(self.model)
        return super().form_valid(form)
    def form_invalid(self, form: forms.RegisterUser) -> HttpResponse:
        return super().form_invalid(form)

class ModelNameList(ListView):
    model = models.UserModel
    queryset = models.UserModel.objects.all()
    template_name='testpages/showData.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    
class CreateUserView(CreateView):
    model = models.UserModel
    fields = ['firstName', 'lastName']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    template_name = 'testpages/create-user.html'
    success_url = '/portfolio/showdata'
    
    def form_valid(self, form: forms.RegisterUser) -> HttpResponse:
        form.save(self.model)
        return super().form_valid(form)
    
class DeleteUserView(DeleteView):
    model = models.UserModel
    template_name = 'testpages/delete-user.html'
    success_url = '/portfolio/showdata'
    
class UpdateUserView(UpdateView):
    model = models.UserModel
    template_name = 'testpages/update-user.html'
    fields = ['firstName', 'lastName']
    success_url = '/portfolio/showdata'

    
    