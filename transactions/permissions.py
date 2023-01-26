from rest_framework.permissions import BasePermission
from rest_framework.views import View, Request
from .models import Transaction
from users.models import User


class IsTransactionOwner(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Transaction):
        obj_owner = User.objects.get(id=obj.user.id)
        return request.user == obj_owner
