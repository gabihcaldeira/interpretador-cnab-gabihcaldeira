from django.urls import path
from . import views

urlpatterns = [
    path("parser/", views.TransactionView.as_view())
]
