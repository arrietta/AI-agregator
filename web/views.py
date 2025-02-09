from djoser.conf import User
from djoser.serializers import UserSerializer
from rest_framework import viewsets


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
