from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import TransactionType, Transaction
from .serializers import TransactionTypeSerializer, TransactionSerializer, ReturnTransactionsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime
import ipdb


class CreateTransactionView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class ListTransactionsView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = ReturnTransactionsSerializer

    def get_queryset(self):
        queryset = Transaction.objects.filter(user_id=self.request.user.id)
        return queryset


class TransactionsByStoreView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        user_transactions = Transaction.objects.filter(user_id=request.user.id)
        data = []
        for store in set(user_transactions.values_list('store_name', flat=True)):
            store_transactions = user_transactions.filter(store_name=store)
            store_inlet = store_transactions.filter(
                transaction_type__kind="IN").aggregate(Sum('value'))
            store_outlet = store_transactions.filter(
                transaction_type__kind="OUT").aggregate(Sum('value'))
            store_balance = (store_inlet['value__sum'] if not store_inlet['value__sum'] == None else Decimal(
                '0.00')) - (store_outlet['value__sum'] if not store_outlet['value__sum'] == None else Decimal('0.00'))
            data.append({
                'store_name': store,
                'store_balance': store_balance
            })

        return Response(data, status.HTTP_200_OK)


class ListTransactionTypes(ListAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
