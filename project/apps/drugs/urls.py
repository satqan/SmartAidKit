from .views import DrugViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', DrugViewSet)

urlpatterns = [
]

urlpatterns += router.urls
