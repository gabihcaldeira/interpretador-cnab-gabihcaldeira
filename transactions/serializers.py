from rest_framework import serializers
from .models import Transaction, TransactionType
from users.models import User
from decimal import Decimal
from datetime import datetime
from django.shortcuts import get_object_or_404


class ReturnTransactionsSerializer(serializers.Serializer):
    id = serializers.CharField()
    value = serializers.CharField()
    transaction_type = serializers.SerializerMethodField()
    date = serializers.CharField()
    time = serializers.CharField()
    card = serializers.CharField()
    cpf = serializers.CharField()
    store_owner = serializers.CharField()
    store_name = serializers.CharField()
    user = serializers.CharField()

    def get_transaction_type(self, obj):
        return obj.transaction_type.type


class TransactionSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    created_transactions = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = [
            'id',
            'date',
            'time',
            'cpf',
            'card',
            'transaction_type',
            'store_name',
            'store_owner',
            'value',
            'user'
        ]

    def get_created_transactions(self, transactions_list):
        serializer = ReturnTransactionsSerializer(transactions_list, many=True)
        return serializer.data

    def create(self, validated_data):
        file = validated_data['file']
        lines_list = [line.decode('utf-8').rstrip() for line in file]
        transactions_list = []
        for line in lines_list:
            line_data = {
                'transaction_type': get_object_or_404(TransactionType, pk=line[0]),
                'date': datetime.strptime(line[1:9], "%Y%m%d").date(),
                'value': Decimal(line[9:19])/Decimal('100.00'),
                'cpf': line[19:30],
                'card': line[30:42],
                'time': datetime.strptime(line[42:48], "%H%M%S").time(),
                'store_owner': line[48:62].rstrip(),
                'store_name': line[62:81],
                'user': User.objects.get(pk=validated_data['user_id'])
            }
            new_obj = Transaction.objects.create(**line_data)
            transactions_list.append(new_obj)

        return transactions_list


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = "__all__"
        read_only_fields = ['type']
