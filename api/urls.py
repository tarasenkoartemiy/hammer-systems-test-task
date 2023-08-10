from django.urls import path
from rest_framework import routers
from .views import UserAPIView, LoginAPIVIew, ActivateAPIView 

urlpatterns = [
    path('login/', LoginAPIVIew.as_view()),
    path('activate/', ActivateAPIView.as_view()),
    path('me/', UserAPIView.as_view())
]
