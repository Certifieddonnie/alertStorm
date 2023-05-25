# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('user/', views.UserView.as_view(), name='user'),
    path('notify/', views.NotifyTypeAPI.as_view(), name='notifications'),
    path('filter/', views.UserListApiView.as_view(), name='filter'),
]
