from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, SaleItemForm
from .models import *
# Create your views here.
class Index(TemplateView):
    template_name = 'inv/index.html'

class Dashboard(LoginRequiredMixin,View):
    def get(self, request):
        items=SaleItem.objects.filter(user=self.request.user.id).order_by('id')
        return render(request, 'inv/dashboard.html', {'items': items})

class Resgiter(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inv/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        return render(request, 'inv/register.html', {'form': form})
    
class AddItem(LoginRequiredMixin, CreateView):
    model=SaleItem
    form_class=SaleItemForm
    template_name='inv/item_form.html'
    success_url=reverse_lazy('dashboard')

    def get_context_data(self, **kwargs): 
        context=super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form) 
    
class EditItem(LoginRequiredMixin, UpdateView):
    model=SaleItem
    form_class=SaleItemForm
    template_name='inv/item_form.html'
    success_url=reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
    model=SaleItem
    template_name='inv/delete_item.html'
    success_url=reverse_lazy('dashboard')
    context_object_name='item'