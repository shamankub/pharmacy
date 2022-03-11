from rest_framework.serializers import ModelSerializer

from .models import SuppliedDrug, Supplier, Supply


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "uuid",
            "name",
            "address",
            "phone",
        ]

class SupplySerializer(ModelSerializer):
    class Meta:
        model = Supply
        fields = [
            "supplier",
            "supply_date",
        ]

class SuppliedDrugSerializer(ModelSerializer):
    class Meta:
        model = SuppliedDrug
        fields = [
            "supply_id",
            "name",
            "quantity",
        ]
