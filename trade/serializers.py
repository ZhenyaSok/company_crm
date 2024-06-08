from rest_framework import serializers, fields
from products.serializers import ProductSerializer

from trade.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField(required=False)
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Trade
        fields = ('id', 'product.json', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        return Trade.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Trade.objects.filter(user_id=obj.user.id).total_quantity()
