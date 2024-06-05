
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trade.apps import TradeConfig
from trade.views import TradeViewSet

app_name = TradeConfig.name

router_trade = DefaultRouter()
router_trade.register(r'trades', TradeViewSet, basename='trades')


urlpatterns = [
    path('', include(router_trade.urls)),

]