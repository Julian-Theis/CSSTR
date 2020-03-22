from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="patients-home"),
    path('registration', views.registration, name="patients-registration"),
    path('activate/',views.activate, name='activate'),
    path('data/', views.data, name="patients-data"),
    path('impress/', views.impress, name="patients-impress"),
]