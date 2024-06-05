
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from contractor.models import Contractor
from contractor.serializers import ContractorSerializer
from products.views import IsActiveUser


class ContractorViewSet(viewsets.ModelViewSet):
    serializer_class = ContractorSerializer
    queryset = Contractor.objects.all()
    filter_backends = [SearchFilter]
    filterset_fields = ['country']
    permission_classes = [IsActiveUser]
