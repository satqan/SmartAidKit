from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Drug
from .serializers import DrugSerializer


class DrugViewSet(ModelViewSet):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    permission_class = IsAuthenticated
