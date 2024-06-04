from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ-панель товара"""
    list_display = ('name', 'category', 'manager', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админ-панель товара"""
    list_display = ('name', 'description', 'created_at')