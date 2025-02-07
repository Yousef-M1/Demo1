from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomerViewSet, CarPartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'carparts', CarPartViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
