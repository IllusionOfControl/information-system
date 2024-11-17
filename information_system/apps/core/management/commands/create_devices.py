import random

from django.core.management.base import BaseCommand
from information_system.apps.core.models import DeviceModel, DeviceInstance, Department, DeviceType


class Command(BaseCommand):
    help = 'Creates device models and instances'

    def handle(self, *args, **options):
        device_types_mapping = {
            dev_type.name: dev_type for dev_type in DeviceType.objects.all()
        }

        device_models = [
            {"manufacturer": "HP", "name": "LaserJet Pro M15w", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Canon", "name": "PIXMA G3411", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Zebra", "name": "ZT230", "type": device_types_mapping.get("Принтер чеков")},
            {"manufacturer": "Epson", "name": "L3150", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Brother", "name": "HL-L2300DR", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Samsung", "name": "Xpress M2070", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Kyocera", "name": "ECOSYS P2040dw", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Xerox", "name": "Phaser 3020BI", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Ricoh", "name": "SP 230DNw", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Konica Minolta", "name": "bizhub C227", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Sharp", "name": "MX-2640N", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Toshiba", "name": "e-STUDIO2505AC", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Lexmark", "name": "MS410d", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "OKI", "name": "B432dn", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Dell", "name": "E525w", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Kodak", "name": "Verité 55 Plus", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Panasonic", "name": "KX-MB2170", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Fujitsu", "name": "ScanSnap iX1500", "type": device_types_mapping.get("Сканер")},
            {"manufacturer": "Canon", "name": "imageRUNNER ADVANCE DX C377i", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "HP", "name": "OfficeJet Pro 8025", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Brother", "name": "MFC-J497DW", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Epson", "name": "WorkForce Pro WF-4720", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Samsung", "name": "SL-M2020", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Kyocera", "name": "MA2000w", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Xerox", "name": "WorkCentre 3335/DNI", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Ricoh", "name": "IM C2000", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Konica Minolta", "name": "bizhub 225i", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Sharp", "name": "MX-B465W", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Toshiba", "name": "e-STUDIO3005AC", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Lexmark", "name": "B2236dw", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "OKI", "name": "MC363dn", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Dell", "name": "S2830dn", "type": device_types_mapping.get("Принтер")},
            {"manufacturer": "Kodak", "name": "SCANMATE i1150", "type": device_types_mapping.get("Сканер")},
            {"manufacturer": "Panasonic", "name": "KX-MB2650", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "HP", "name": "LaserJet Pro MFP M28w", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Canon", "name": "MAXIFY MB5440", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Brother", "name": "DCP-L2550DW", "type": device_types_mapping.get("МФУ")},
            {"manufacturer": "Epson", "name": "EcoTank ET-2720", "type": device_types_mapping.get("МФУ")}
        ]

        departments = Department.objects.all()
        if not departments:
            self.stdout.write(self.style.ERROR('No departments found. Create departments first.'))
            return

        for model_data in device_models:
            device_model, created = DeviceModel.objects.get_or_create(**model_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created device model "{device_model}"'))

            # Создаем экземпляры устройств для каждой модели
            for i in range(random.randint(2, 5)):  # Случайное количество экземпляров от 2 до 5
                inventory_number = f"{device_model.name}-{random.randint(1000, 9999)}"
                department = random.choice(departments)
                device_instance, created = DeviceInstance.objects.get_or_create(
                    device_model=device_model,
                    inventory_number=inventory_number,
                    department=department,
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created device instance "{device_instance}"'))
                else:
                    self.stdout.write(self.style.WARNING(f'Device instance "{device_instance}" already exists'))
