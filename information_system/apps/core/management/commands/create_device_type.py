from django.core.management.base import BaseCommand
from information_system.apps.core.models import DeviceType


class Command(BaseCommand):
    help = 'Creates device types'

    def handle(self, *args, **options):
        device_types = [
            "Принтер",
            "МФУ",
            "Сканер",
            "Компьютер",
            "Монитор",
            "Ноутбук",
            "Планшет",
            "Смартфон",
            "Сервер",
            "Коммутатор",
            "Роутер",
            "IP-камера",
            "Проектор",
            "Интерактивная доска",
            "Кассовый аппарат",
            "Терминал сбора данных",
            "POS-терминал",
            "Электронные весы",
            "Принтер чеков",
            "Считыватель штрих-кодов"
        ]

        for device_type in device_types:
            DeviceType.objects.get_or_create(name=device_type)
            self.stdout.write(self.style.SUCCESS(f'Successfully created device type "{device_type}"'))
