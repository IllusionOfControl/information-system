import random
from datetime import timedelta, datetime

from django.core.management.base import BaseCommand

from information_system.apps.core.models import DeviceInstance, Repair, User, \
    MalfunctionType


class Command(BaseCommand):
    help = 'Creates device repairs'

    def handle(self, *args, **options):
        devices = list(DeviceInstance.objects.all())
        malfunction_types = list(MalfunctionType.objects.all())
        users = list(
            User.objects.filter(role__in=['master', 'administrator']))  # Выбираем только мастеров и администраторов

        if not devices or not malfunction_types or not users:
            print(
                "Недостаточно данных для генерации. Убедитесь, что есть устройства, типы неисправностей и пользователи (мастера или администраторы).")
            return

        for _ in range(1000):
            date_breakdown = datetime.now() - timedelta(
                days=random.randint(0, 365))  # Случайная дата в течение последнего года
            device_instance = random.choice(devices)
            malfunction_type = random.choice(malfunction_types)
            performed_by = random.choice(users)
            date_repair = date_breakdown + timedelta(
                days=random.randint(1, 10)) if random.random() < 0.8 else None  # 80% ремонтов завершены
            note = random.choice(["Замена детали", "Чистка", "Настройка", "Перепрошивка", ""])

            Repair.objects.create(
                date_breakdown=date_breakdown,
                device_instance=device_instance,
                malfunction_type=malfunction_type,
                date_repair=date_repair,
                performed_by=performed_by,
                note=note,
            )
