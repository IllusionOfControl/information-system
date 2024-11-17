import os
import random

from django.conf import settings

from information_system.apps.core.models import Department

def create_departments(num_departments=30):
    """
    Создает указанное количество ОПС с номерами от 1 до 30.
    Если ОПС с таким номером уже существует, он будет пропущен.
    """

    for i in range(1, num_departments + 1):
        try:
            # Проверяем, существует ли уже ОПС с таким номером
            Department.objects.get(name=f"ОПС-{i}")
            print(f"ОПС-{i} уже существует. Пропускаем.")
        except Department.DoesNotExist:
            # Создаем новое ОПС
            department = Department(
                name=f"ОПС-{i}",
                index=f"{random.randint(10000, 99999)}",  # Случайный индекс
                phone=f"+{random.randint(1000000000, 9999999999)}",  # Случайный телефон
                type=random.choice(['city', 'village']),  # Случайный тип
                district=f"Район-{random.randint(1, 10)}"  # Случайный район
            )
            department.save()
            print(f"ОПС-{i} создан.")


# Вызываем функцию для создания 30 ОПС:
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "information_system.settings")
    create_departments()