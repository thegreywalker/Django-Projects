from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:month>", views.monthly_challenge_by_number, name="Monthly_Challenge_By_Number"),
    path("<str:month>", views.monthly_challenge, name="Monthly_Challenge"),
    
]