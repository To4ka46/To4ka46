from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r"collects", CollectViewSet)
# вложенные пути для платежей лучше делать отдельным роутом и фильтровать по collect_pk в view
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
