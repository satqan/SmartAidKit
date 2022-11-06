from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Kit
from .serializers import KitSerializer


class KitViewSet(ModelViewSet):
    serializer_class = KitSerializer
    queryset = Kit.objects.all()
    permission_class = IsAuthenticated
