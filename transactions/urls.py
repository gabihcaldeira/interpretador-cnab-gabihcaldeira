from django.urls import path
from . import views

urlpatterns = [
    path("parser/", views.TransactionView.as_view()),
    path("teste/", views.ListTransactionTypes.as_view())
]
