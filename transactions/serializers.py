from rest_framework import serializers
from .models import Transaction, TransactionType
from decimal import Decimal
from datetime import datetime
import ipdb


class TransactionSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = [
            'id',
            'description',
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

    def create(self, validated_data):
        # ipdb.set_trace()
        file = validated_data['file']
        lines_list = [line.decode('utf-8').rstrip() for line in file]
        data = []
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
                'user': validated_data['user_id']
            }
            data.append(Transaction.objects.create(line_data))

        return data


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = "__all__"
        read_only_fields = ['type']
