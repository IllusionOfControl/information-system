import random
from datetime import timedelta, datetime

from django.core.management.base import BaseCommand

from information_system.apps.core.models import DeviceInstance, Repair, User, \
    MalfunctionType, MaintenanceType, Maintenance


class Command(BaseCommand):
    help = 'Creates device maintenances'

    def handle(self, *args, **options):
        devices = list(DeviceInstance.objects.all())
        maintenance_types = list(MaintenanceType.objects.all())
        users = list(User.objects.filter(role__in=['master']))

        if not devices or not maintenance_types or not users:
            print(
                "Недостаточно данных для генерации. Убедитесь, что есть устройства, типы обслуживания и пользователи (мастера или администраторы).")
            return

        for _ in range(1000):
            date = datetime.now() - timedelta(days=random.randint(0, 365))
            device = random.choice(devices)
            maintenance_type = random.choice(maintenance_types)
            performed_by = random.choice(users)
            note = random.choice(["Замена фильтра", "Чистка", "Проверка работоспособности", "Калибровка", ""])

            Maintenance.objects.create(
                date=date,
                device_instance=device,
                type=maintenance_type,
                performed_by=performed_by,
                note=note,
            )

        print(f"Сгенерировано {1000} записей технического обслуживания.")