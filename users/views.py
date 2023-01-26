from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner, IsAuthenticatedOrCreate
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrCreate]

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset


class UpdateDestroyUserView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
