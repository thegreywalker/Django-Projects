from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logoutx', views.logoutx, name="logoutx"),
    path('dashboard', views.dashboard, name="dashboard")
]