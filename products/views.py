from rest_framework import viewsets, permissions

from products.models import Product, Category
from products.serializers import ProductSerializers, CategorySerializers


class IsActiveUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [IsActiveUser]
