from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from products.apps import ProductsConfig
from products.views import ProductViewSet, CategoryViewSet

app_name = ProductsConfig.name

router_product = DefaultRouter()
router_product.register(r'product', ProductViewSet, basename='product')

router_category = DefaultRouter()
router_category.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router_product.urls)),
    path('', include(router_category.urls)),
]