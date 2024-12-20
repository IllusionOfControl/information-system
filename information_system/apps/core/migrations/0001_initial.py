# Generated by Django 5.1.2 on 2024-10-22 22:11

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("index", models.CharField(max_length=10, verbose_name="Индекс")),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("city", "Городское"), ("village", "Сельское")],
                        max_length=20,
                        verbose_name="Тип",
                    ),
                ),
                ("district", models.CharField(max_length=255, verbose_name="Район")),
            ],
        ),
        migrations.CreateModel(
            name="DeviceModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Модель")),
                (
                    "manufacturer",
                    models.CharField(max_length=255, verbose_name="Производитель"),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
        ),
        migrations.CreateModel(
            name="DeviceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название типа"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MaintenanceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название типа ТО"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MalfunctionType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название неисправности"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("FIO", models.CharField(max_length=255, verbose_name="ФИО")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("administrator", "Администратор"),
                            ("master", "Мастер"),
                            ("inspector", "Проверяющий"),
                        ],
                        max_length=20,
                        verbose_name="Роль",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="DeviceInstance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "inventory_number",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Инвентарный номер"
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.department",
                        verbose_name="Отделение связи",
                    ),
                ),
                (
                    "device_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.devicemodel",
                        verbose_name="Модель устройства",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="devicemodel",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="core.devicetype",
                verbose_name="Тип",
            ),
        ),
        migrations.CreateModel(
            name="Maintenance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Дата")),
                ("note", models.TextField(blank=True, verbose_name="Примечание")),
                (
                    "device_instance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.deviceinstance",
                        verbose_name="Устройство",
                    ),
                ),
                (
                    "performed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Работу выполнил",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.maintenancetype",
                        verbose_name="Вид ТО",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Repair",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_breakdown", models.DateField(verbose_name="Дата поломки")),
                (
                    "date_repair",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата устранения поломки"
                    ),
                ),
                ("note", models.TextField(blank=True, verbose_name="Примечание")),
                (
                    "device_instance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.deviceinstance",
                        verbose_name="Устройство",
                    ),
                ),
                (
                    "malfunction_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.malfunctiontype",
                        verbose_name="Характер неисправности",
                    ),
                ),
                (
                    "performed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Работу выполнил",
                    ),
                ),
            ],
        ),
    ]
