from rest_framework import mixins, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import SuppliedDrug, Supplier, Supply
from .serializers import (SuppliedDrugSerializer, SupplierSerializer,
                          SupplySerializer)


class SuppliedDrugModelViewSet(ModelViewSet):
    queryset = SuppliedDrug.objects.all()
    serializer_class = SuppliedDrugSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class SupplierModelViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class SupplyModelViewSet(ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
