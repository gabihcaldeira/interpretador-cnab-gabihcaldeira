from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import TransactionType, Transaction
from .serializers import TransactionTypeSerializer, TransactionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTransactionOwner
from decimal import Decimal
from datetime import datetime
import ipdb


class TransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = [TransactionSerializer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTransactionOwner]

    def create(self, request: Request, *args, **kwargs):
        file_request = request.FILES['file']
        lines_list = [line.decode('utf-8').rstrip() for line in file_request]
        request.data = []
        for line in lines_list:
            line_data = {
                'transaction_type': line[0],
                'date': datetime.strptime(line[1:9], "%Y%m%d").date(),
                'value': Decimal(line[9:19]),
                'cpf': line[19:30],
                'card': line[30:42],
                'time': datetime.strptime(line[42:48], "%H%M%S").time(),
                'store_owner': line[48:62].rstrip(),
                'store_name': line[62:81],
                'user': request.user.id
            }
            request.data.append(line_data)

        serializer = TransactionSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().create(request, *args, **kwargs)


class ListTransactionTypes(ListAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
