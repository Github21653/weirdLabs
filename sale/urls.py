
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('additem/', AddItem.as_view(), name='additem'),
    path('edititem/<int:pk>', EditItem.as_view(), name='edititem'),
    path('deleteitem/<int:pk>', DeleteItem.as_view(), name='deleteitem'),
    path('register/', Resgiter.as_view(), name='register'),   
    path('login/', auth_views.LoginView.as_view(template_name='inv/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inv/logout.html'), name='logout'),
]