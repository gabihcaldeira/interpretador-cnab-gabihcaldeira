from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import TransactionType, Transaction
from .serializers import TransactionTypeSerializer, TransactionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime


class CreateTransactionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        file_request = request.FILES['file']
        lines_list = [line.decode('utf-8').rstrip() for line in file_request]
        request_data = []
        for line in lines_list:
            line_data = {
                'transaction_type': line[0],
                'date': datetime.strptime(line[1:9], "%Y%m%d").date(),
                'value': Decimal(line[9:19])/Decimal('100.00'),
                'cpf': line[19:30],
                'card': line[30:42],
                'time': datetime.strptime(line[42:48], "%H%M%S").time(),
                'store_owner': line[48:62].rstrip(),
                'store_name': line[62:81],
                'user': request.user.id
            }
            request_data.append(line_data)

        serializer = TransactionSerializer(data=request_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        transactions_list = Transaction.objects.filter(user_id=request.user.id)
        serializer = TransactionSerializer(transactions_list, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


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


class ListTransactionTypes(ListCreateAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
