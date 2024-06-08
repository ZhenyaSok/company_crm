from rest_framework import serializers
from contractor.models import Contractor
from products.models import Product


class ContractorSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source="address.get_complete_address", read_only=True)
    list_products = serializers.SerializerMethodField()
    debt = serializers.CharField(read_only=True)
    read_only_fields = ('debt',)  # Нельзя редактировать поле задолженности со стороны API

    def get_list_products(self, contractor):
        """Метод выводит все товары которые может реализовать поставщик"""
        list = []
        for product in Product.objects.filter(contractor=contractor):
            a = f"{product.name} модель {product.model_product}, цена {product.price}, дата выхода {product.created_at}"
            list.append(a)
        return list
        # return [product.name for product in Product.objects.filter(contractor=contractor)]

    class Meta:
        model = Contractor
        fields = '__all__'