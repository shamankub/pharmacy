from uuid import uuid4

# from django.contrib.auth.models import AbstractUser
from django.db import models


# Должности
class Position(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="название должности")
    experience = models.CharField(max_length=1, choices=(("1", "1"), ("2", "2"), ("3", "3"),), verbose_name="требуемый опыт (лет)")
    salary = models.BigIntegerField(unique=True, verbose_name="оклад")

    def __str__(self):
        return self.name

# Филиалы
class Branch(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="название филиала")
    branch_head = models.CharField(max_length=64, verbose_name="руководитель")
    address = models.CharField(max_length=200, verbose_name="адрес")
    phone = models.BigIntegerField(unique=True, verbose_name="телефон")
    
    def __str__(self):
        return self.name

# Сотрудники
class Staff(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, verbose_name="UUID")
    first_name = models.CharField(max_length=64, verbose_name="имя")
    last_name = models.CharField(max_length=64, verbose_name="фамилия")
    patronymic = models.CharField(max_length=64, verbose_name="отчество")
    passport_num = models.BigIntegerField(unique=True, null=False, verbose_name="серия и номер паспорта")
    passport_date = models.DateField(null=False, verbose_name="дата выдачи паспорта")
    address = models.CharField(max_length=200, verbose_name="адрес")
    phone = models.BigIntegerField(unique=True, verbose_name='телефон')
    email = models.EmailField(unique=True, max_length=254, null=False, verbose_name="электронная почта")
    branch = models.ForeignKey(Branch, null=False, on_delete=models.PROTECT, verbose_name="филиал")
    position = models.ForeignKey(Position, null=False, on_delete=models.PROTECT, verbose_name="должность")

    def __str__(self):
        return " ".join([self.last_name, self.first_name, self.patronymic])

# Отпуска    
class Vacation(models.Model):
    staff_id = models.ForeignKey(Staff, null=False, on_delete=models.CASCADE, verbose_name="ID сотрудника")
    vacation_start = models.DateField(null=False, verbose_name="начало отпуска")
    vacation_end = models.DateField(null=False, verbose_name="конец отпуска")

# Зарплаты
class Salary(models.Model):
    staff_id = models.ForeignKey(Staff, null=False, on_delete=models.CASCADE, verbose_name="ID сотрудника")
    salary_date = models.DateField(null=False, verbose_name="дата выплаты зарплаты")
    salary = models.BigIntegerField(null=False, verbose_name="зарплата")
    salary_bonus = models.BigIntegerField(default=0, verbose_name="премия")
