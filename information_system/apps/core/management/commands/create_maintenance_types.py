from django.core.management.base import BaseCommand

from information_system.apps.core.models import MaintenanceType


class Command(BaseCommand):
    help = 'Creates device maintenances'

    def handle(self, *args, **options):
        maintenance_types_data = [
            "Чистка",
            "Обновление ПО",
            "Плановое обслуживание",
        ]

        for maintenance_name in maintenance_types_data:
            MaintenanceType.objects.get_or_create(name=maintenance_name)
