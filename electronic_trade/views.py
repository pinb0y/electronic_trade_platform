from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from electronic_trade.models import Supplier
from electronic_trade.permissions import ActiveUserPermission
from electronic_trade.serializers import SupplierSerializer, DetailSupplierSerializer, EditSupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('contacts__country',)
    permission_classes = (ActiveUserPermission,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(DetailSupplierSerializer(instance).data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailSupplierSerializer
        if self.action in ['update', 'partial_update']:
            return EditSupplierSerializer
        return SupplierSerializer
