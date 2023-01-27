from django.urls import path
from . import views

urlpatterns = [
    path("parser/", views.CreateTransactionView.as_view()),
    path("transaction/types/", views.ListTransactionTypes.as_view()),
    path("stores/transactions/", views.TransactionsByStoreView.as_view())
]
