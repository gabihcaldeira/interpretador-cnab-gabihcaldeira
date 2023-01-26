from rest_framework.permissions import BasePermission
from rest_framework.views import View, Request
from users.models import User


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return request.user == obj


class IsAuthenticatedOrCreate(BasePermission):
    def has_permission(self, request: Request, view: View):
        return (request.method == 'POST' or request.user and
                request.user.is_authenticated)
