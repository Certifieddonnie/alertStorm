# from django.conf.urls import url
from django.urls import path, include, re_path
from knox import views as knox_views
from .views import (
    UserListApiView, RegisterAPI, LoginAPI
)

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('countries/', UserListApiView.as_view()),
]
