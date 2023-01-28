from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path("parser/", views.CreateTransactionView.as_view()),
    path("transaction/types/", views.ListTransactionTypes.as_view()),
    path("transactions/", views.ListTransactionsView.as_view()),
    path("stores/transactions/", views.TransactionsByStoreView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name='schema'),
    path("docs/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
