import random
from datetime import timedelta, datetime

from django.core.management.base import BaseCommand

from information_system.apps.core.models import DeviceInstance, Repair, User, \
    MalfunctionType


class Command(BaseCommand):
    help = 'Creates device repairs'

    def handle(self, *args, **options):
        malfunction_types_data = [
            "Не включается",
            "Проблемы с сетью",
            "Проблемы с программным обеспечением",
            "Механические повреждения",
            "Требуется чистка",
            "Зависает",
            "Перегревается",
            "Шумит",
        ]

        for malfunction_name in malfunction_types_data:
            MalfunctionType.objects.get_or_create(name=malfunction_name)
