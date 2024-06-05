from django.urls import include, path
from rest_framework.routers import DefaultRouter

from contractor.apps import ContractorConfig
from contractor.views import ContractorViewSet

app_name = ContractorConfig.name

contractors_router = DefaultRouter()
contractors_router.register(r'contractors', ContractorViewSet, basename='contractors')

urlpatterns = [
    path('', include(contractors_router.urls)),
]