from django.urls import path, include
from rest_framework.routers import DefaultRouter

from electronic_trade.apps import ElectronicTradeConfig
from electronic_trade.views import SupplierViewSet

app_name = ElectronicTradeConfig.name

router = DefaultRouter()
router.register('supplier', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
