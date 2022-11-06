from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
