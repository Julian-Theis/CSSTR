from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="staff-home"),
    path('login/', auth_views.LoginView.as_view(template_name="staff/login.html"), name="staff-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="staff/logout.html"), name="staff-logout")
]