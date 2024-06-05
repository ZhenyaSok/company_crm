from rest_framework import serializers

from products.models import Product
from trade.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    # list_products = serializers.SerializerMethodField()
    price = serializers.CharField(source="product.get_complete_address", read_only=True)
    summ = serializers.FloatField(source="trade.all_summ", read_only=True)


    def get_price(self, trade):
        return [product.price for product in Product.objects.filter(trade=trade)]

    class Meta:
        model = Trade
        fields = ("price", 'summ')