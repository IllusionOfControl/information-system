from django.contrib import admin

from .models import (
    User,
    Department,
    DeviceType,
    DeviceModel,
    DeviceInstance,
    MaintenanceType,
    Maintenance,
    MalfunctionType,
    Repair
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'FIO', 'email', 'phone', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')
    search_fields = ('username', 'FIO', 'email')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'index', 'phone', 'type', 'district')
    list_filter = ('type',)
    search_fields = ('name', 'index')


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(DeviceModel)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)


@admin.register(DeviceInstance)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('inventory_number', 'device_model', 'department')
    list_filter = ('device_model', 'department')
    search_fields = ('inventory_number',)

@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'device_instance', 'type', 'performed_by', 'note')
    list_filter = ('date', 'type', 'performed_by', 'device_instance__department')
    search_fields = ('device_instance__device_model__name', 'note')


@admin.register(MalfunctionType)
class MalfunctionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('date_breakdown', 'device_instance', 'malfunction_type', 'date_repair', 'performed_by', 'note')
    list_filter = ('date_breakdown', 'date_repair', 'malfunction_type', 'performed_by', 'device_instance__department')
    search_fields = ('device_instance__device_model__name', 'note')
