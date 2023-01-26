from rest_framework import serializers
from .models import Transaction, TransactionType


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only = ['id']


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = "__all__"
        read_only_fields = ['type']
