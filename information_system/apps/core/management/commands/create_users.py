from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from information_system.apps.core.models import User


class Command(BaseCommand):
    help = 'Creates device repairs'

    def handle(self, *args, **options):
        users_data = [
            {"username": "admin", "password": "adminpassword", "role": "administrator",
             "FIO": "Администратор Системный"},
            {"username": "master1", "password": "masterpassword", "role": "master", "FIO": "Мастер Иванов"},
            {"username": "master2", "password": "masterpassword", "role": "master", "FIO": "Мастер Петров"},
            {"username": "inspector1", "password": "inspectorpassword", "role": "inspector",
             "FIO": "Проверяющий Сидоров"},
        ]

        for user_data in users_data:
            try:
                user = User.objects.get(username=user_data['username'])
                print(f"Пользователь {user_data['username']} уже существует. Обновляем данные...")
                # Обновляем данные пользователя, если он уже существует
                user.password = make_password(user_data['password'])
                user.role = user_data['role']
                user.FIO = user_data['FIO']
                user.save()


            except User.DoesNotExist:
                print(f"Создаем пользователя {user_data['username']}...")

                User.objects.create_user(
                    username=user_data['username'],
                    password=user_data['password'],
                    role=user_data['role'],
                    FIO=user_data['FIO']
                )
