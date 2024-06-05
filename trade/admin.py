from django.contrib import admin

from trade.models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'contractor', 'quantity', 'payment_method', 'payment_summ', 'is_approved')

