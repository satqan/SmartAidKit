from .views import KitViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'', KitViewSet)

urlpatterns = [
]

urlpatterns += router.urls
