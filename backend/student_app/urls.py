from django.urls import path

from .views import home, login_view, logout_view, register_view, course_detail, profile_view, submission_view


from backend.views import base

urlpatterns = [
    path('t', base, name='base'),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('course/detail/<int:pk>/', course_detail, name='course_detail'),
    path('submission/<int:pk>', submission_view, name='submission'),
]
