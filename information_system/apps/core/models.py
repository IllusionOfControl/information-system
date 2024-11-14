from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя системы, расширяющая стандартную модель Django.
    """
    FIO = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    ROLE_CHOICES = (
        ('administrator', 'Администратор'),
        ('master', 'Мастер'),
        ('inspector', 'Проверяющий'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Роль")


class Department(models.Model):
    """
    Модель для хранения информации об отделениях почтовой связи.
    """
    name = models.CharField(max_length=255, verbose_name="Название")
    index = models.CharField(max_length=10, verbose_name="Индекс")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    TYPE_CHOICES = (
        ('city', 'Городское'),
        ('village', 'Сельское'),
        # ... другие типы отделений
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип")
    district = models.CharField(max_length=255, verbose_name="Район")

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    """
    Модель для хранения типов устройств.
    """
    name = models.CharField(max_length=255, verbose_name="Название типа")

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    """Модель устройства (общая информация)"""
    name = models.CharField(max_length=255, verbose_name="Модель")
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель")
    description = models.TextField(blank=True, verbose_name="Описание")
    type = models.ForeignKey(DeviceType, on_delete=models.PROTECT, verbose_name="Тип")

    def __str__(self):
        return f"{self.manufacturer} {self.name}"


class DeviceInstance(models.Model):
    """Экземпляр устройства (конкретное устройство)"""
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, verbose_name="Модель устройства")
    inventory_number = models.CharField(max_length=255, unique=True, verbose_name="Инвентарный номер")
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="Отделение связи")

    def __str__(self):
        return f"{self.device_model} ({self.inventory_number})"


class MaintenanceType(models.Model):
    """
    Модель для хранения типов технического обслуживания.
    """
    name = models.CharField(max_length=255, verbose_name="Название типа ТО")

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    """
    Модель для хранения информации о техническом обслуживании.
    """
    date = models.DateField(verbose_name="Дата")
    device_instance = models.ForeignKey(DeviceInstance, on_delete=models.CASCADE, verbose_name="Устройство")
    type = models.ForeignKey(MaintenanceType, on_delete=models.PROTECT, verbose_name="Вид ТО")
    performed_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Работу выполнил")
    note = models.TextField(blank=True, verbose_name="Примечание")


class MalfunctionType(models.Model):
    """
    Модель для хранения типов неисправностей.
    """
    name = models.CharField(max_length=255, verbose_name="Название неисправности")

    def __str__(self):
        return self.name


class Repair(models.Model):
    """
    Модель для хранения информации о ремонтах.
    """
    date_breakdown = models.DateField(verbose_name="Дата поломки")
    device_instance = models.ForeignKey(DeviceInstance, on_delete=models.CASCADE, verbose_name="Устройство")
    malfunction_type = models.ForeignKey(MalfunctionType, on_delete=models.PROTECT,
                                         verbose_name="Характер неисправности")
    date_repair = models.DateField(null=True, blank=True, verbose_name="Дата устранения поломки")
    performed_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Работу выполнил")
    note = models.TextField(blank=True, verbose_name="Примечание")
