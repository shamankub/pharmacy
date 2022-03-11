from uuid import uuid4

from django.db import models
from employeeapp.models import Branch


# Форма выпуска
class FormOfRelease(models.Model):
    name = models.CharField(max_length=64, verbose_name="форма выпуска")

    def __str__(self):
        return self.name

# Препараты
class Drug(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, verbose_name="UUID")
    name = models.CharField(max_length=64, verbose_name="препарат")
    form_of_release = models.ForeignKey(FormOfRelease, null=False, on_delete=models.PROTECT, verbose_name="форма выпуска")
    cost = models.BigIntegerField(null=False, verbose_name="стоимость")
    branch = models.ForeignKey(Branch, null=False, on_delete=models.PROTECT, verbose_name="филиал")
    recipe = models.BooleanField(default=False, verbose_name="рецепт")
    indications = models.TextField(verbose_name="показания")
    storage_conditions = models.TextField(verbose_name="условия хранения")

    def __str__(self):
        return self.name

# Пациенты
class Patient(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, verbose_name="UUID")
    first_name = models.CharField(max_length=64, verbose_name="имя")
    last_name = models.CharField(max_length=64, verbose_name="фамилия")
    patronymic = models.CharField(max_length=64, verbose_name="отчество")
    birthday_date = models.DateField(null=False, verbose_name="дата рождения")

    def __str__(self):
        return " ".join([self.last_name, self.first_name, self.patronymic])

# Рецепты
class Recipe(models.Model):
    patient = models.ForeignKey(Patient, null=False, on_delete=models.PROTECT, verbose_name="пациент")
    recipe_date = models.DateTimeField(auto_now_add=True, verbose_name="дата рецепта")

# Препараты по рецепту
class PrescriptionDrug(models.Model):
    name = models.ForeignKey(Drug, null=False, on_delete=models.PROTECT, verbose_name="препарат")
    recipe_id = models.ForeignKey(Recipe, null=False, on_delete=models.PROTECT, verbose_name="номер рецепта")
    quantity = models.BigIntegerField(null=False, verbose_name="количество")
