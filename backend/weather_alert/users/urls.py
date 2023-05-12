# from django.conf.urls import url
from django.urls import path, include
from .views import (
    UserListApiView,
)

urlpatterns = [
    path('', UserListApiView.as_view()),
]
