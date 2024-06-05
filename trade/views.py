
from rest_framework import viewsets

from products.views import IsActiveUser
from trade.models import Trade
from trade.serializers import TradeSerializer


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    queryset = Trade.objects.all()
    permission_classes = [IsActiveUser]
