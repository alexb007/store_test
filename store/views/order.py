from rest_framework import viewsets

from core.permissions import ApiKeyPermission
from store.models import Order
from store.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [ApiKeyPermission]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('created_at', 'updated_at')
