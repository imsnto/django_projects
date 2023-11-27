from django.urls import path

from .views import home, login_view, logout_view, register_view
from django.contrib.auth.views import LoginView, LogoutView


from backend.views import base

urlpatterns = [
    path('t', base, name='base'),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
