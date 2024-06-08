
from rest_framework import viewsets

from products.views import IsActiveUser
from trade.models import Trade
from trade.serializers import TradeSerializer


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    queryset = Trade.objects.all()
    permission_classes = [IsActiveUser]


# @login_required
# def trade_add(request, product_id):
#     Trade.create_or_update(product_id, request.user)
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
#
# @login_required
# def trade_remove(request, basket_id):
#     basket = Trade.objects.get(id=basket_id)
#     basket.delete()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])