from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
