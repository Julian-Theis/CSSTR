from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="patients-home"),
    path('registration', views.registration, name="patients-registration"),
]