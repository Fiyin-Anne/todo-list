from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('edit_task/<str:pk>/', views.editTask, name='edit_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]