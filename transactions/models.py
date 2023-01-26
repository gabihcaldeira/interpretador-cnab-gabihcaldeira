from django.db import models
import uuid


class TransactionType(models.Model):
    type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    kind = models.CharField(max_length=7, choices=[
                            ("IN", "inlet"), ("OUT", "outlet")])
    sign = models.CharField(max_length=1, choices=[("+", "+"), ("-", "-")])


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date = models.DateField()
    value = models.DecimalField(decimal_places=2, max_digits=30)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    time = models.TimeField()
    store_owner = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    transaction_type = models.ForeignKey(
        "transactions.TransactionType", on_delete=models.CASCADE, related_name="transactions")
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='transactions')
