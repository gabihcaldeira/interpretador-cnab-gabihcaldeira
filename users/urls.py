from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.ListCreateUserView.as_view()),
    path("users/<str:pk>/", views.RetrieveUpdateDestroyUserView.as_view()),
    path("login/", TokenObtainPairView.as_view())
]
