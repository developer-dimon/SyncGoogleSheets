from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from synchronization.api.serializers import OrderSerializer
from synchronization.models import Order
from synchronization.services import update_orders_db


@api_view(['POST'])
def update_data(request):
    update_orders_db()
    return Response(status=200)


class OrderViewSet(ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        return get_object_or_404(Order, order_number=self.kwargs.get('pk'))