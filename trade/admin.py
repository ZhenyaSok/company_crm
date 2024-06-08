from django.contrib import admin

from trade.models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('product', 'contractor', 'quantity', 'created_timestamp')


# class TradeAdmin(admin.TabularInline):
#     model = Trade
#     fields = ('product.json', 'contractor', 'quantity', 'created_timestamp')
#     readonly_fields = ('created_timestamp',)
#     extra = 0

