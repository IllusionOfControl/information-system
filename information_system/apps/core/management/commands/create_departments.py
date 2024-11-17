# your_app/management/commands/create_departments.py

from django.core.management.base import BaseCommand
from information_system.apps.core.models import Department


class Command(BaseCommand):
    help = 'Creates departments with numbers from 1 to 30'

    def handle(self, *args, **options):
        department_type = "Городское"  # или любой другой тип по умолчанию
        district = "Не указан"  # или любой другой район по умолчанию

        for i in range(1, 31):
            department_name = f"ОПС-{i}"
            department, created = Department.objects.get_or_create(
                name=department_name,
                defaults={
                    'index': str(10000 + i),  # Пример индекса, можно изменить
                    'phone': f"+123456789{i}",  # Пример номера телефона
                    'type': department_type,
                    'district': district,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created department "{department_name}"'))
            else:
                self.stdout.write(self.style.WARNING(f'Department "{department_name}" already exists'))
