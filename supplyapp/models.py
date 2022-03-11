from uuid import uuid4

from django.db import models
from drugsapp.models import Drug


# Поставщики
class Supplier(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, verbose_name="UUID")
    name = models.CharField(max_length=64, verbose_name="поставщик")
    address = models.CharField(max_length=200, verbose_name="адрес")
    phone = models.BigIntegerField(unique=True, verbose_name='телефон')

    def __str__(self):
        return self.name

# Поставки
class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, null=False, on_delete=models.PROTECT, verbose_name="поставщик")
    supply_date = models.DateTimeField(auto_now_add=True, verbose_name="дата поставки")

# Поставляемые препараты
class SuppliedDrug(models.Model):
    supply_id = models.ForeignKey(Supply, null=False, on_delete=models.PROTECT, verbose_name="поставщик")
    name = models.ForeignKey(Drug, null=False, on_delete=models.PROTECT, verbose_name="препарат")
    quantity = models.BigIntegerField(null=False, verbose_name="количество")
