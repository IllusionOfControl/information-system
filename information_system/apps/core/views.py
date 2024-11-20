import openpyxl
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from information_system.apps.core.models import Department, DeviceModel, DeviceInstance, DeviceType, Repair, \
    Maintenance, MalfunctionType, User


def index(request):
    return render(request, 'core/index.html')


def department_list(request):
    departments = Department.objects.all()
    selected_department = None
    devices_in_department = []

    if request.GET.get('department'):
        selected_department = get_object_or_404(Department, pk=request.GET.get('department'))
        devices_in_department = DeviceInstance.objects.filter(department=selected_department).select_related(
            'device_model')

    context = {
        'departments': departments,
        'selected_department': selected_department,
        'devices_in_department': devices_in_department,
    }
    return render(request, 'core/department_list.html', context)


def device_list(request):
    devices = DeviceModel.objects.all()
    context = {'devices': devices}
    return render(request, 'core/device_list.html', context)


def device_model_list(request):
    device_models = DeviceModel.objects.all().select_related('type')
    device_types = DeviceType.objects.all()
    selected_device_model = None
    device_instances = []

    if request.GET.get('device_type'):
        selected_device_type = get_object_or_404(DeviceType, pk=request.GET.get('device_type'))
        device_instances = DeviceInstance.objects.filter(device_model__type=selected_device_type).select_related(
            'device_model')

    if request.GET.get('device_model'):
        selected_device_model = get_object_or_404(DeviceModel, pk=request.GET.get('device_model'))
        device_instances = DeviceInstance.objects.filter(device_model=selected_device_model)

    context = {
        'device_models': device_models,
        'device_types': device_types,
        'selected_device_model': selected_device_model,
        'device_instances': device_instances,
    }
    return render(request, 'core/device_model_list.html', context)


def repair_list(request):
    queryset = Repair.objects.all().select_related(
        'device_instance', 'device_instance__device_model', 'performed_by', "malfunction_type"
    )

    device_name = request.GET.get('device_name')
    date_breakdown_start = request.GET.get('date_breakdown_start')
    date_breakdown_end = request.GET.get('date_breakdown_end')
    device_type = request.GET.get('device_type')
    malfunction_type = request.GET.get('malfunction_type')
    performed_by = request.GET.get('performed_by')

    if device_name:
        queryset = queryset.filter(device_instance__name__icontains=device_name)

    if date_breakdown_start:
        queryset = queryset.filter(date_breakdown__gte=date_breakdown_start)

    if date_breakdown_end:
        queryset = queryset.filter(date_breakdown__lte=date_breakdown_end)

    if device_type:
        queryset = queryset.filter(device_instance__device_model__type_id=device_type)

    if malfunction_type:
        queryset = queryset.filter(malfunction_type_id=malfunction_type)

    if performed_by:
        queryset = queryset.filter(performed_by_id=performed_by)

    repairs = queryset
    device_types = DeviceType.objects.all()
    malfunction_types = MalfunctionType.objects.all()
    users = User.objects.all()

    context = {'repairs': repairs, 'device_types': device_types, 'malfunction_types': malfunction_types, 'users': users}
    return render(request, 'core/repair_list.html', context)


def export_repairs_to_excel(request):
    queryset = Repair.objects.all().select_related(
        'device_instance', 'device_instance__device_model', 'performed_by', "malfunction_type"
    )

    device_name = request.GET.get('device_name')
    date_breakdown_start = request.GET.get('date_breakdown_start')
    date_breakdown_end = request.GET.get('date_breakdown_end')
    device_type = request.GET.get('device_type')
    malfunction_type = request.GET.get('malfunction_type')
    performed_by = request.GET.get('performed_by')

    if device_name:
        queryset = queryset.filter(device_instance__name__icontains=device_name)

    if date_breakdown_start:
        queryset = queryset.filter(date_breakdown__gte=date_breakdown_start)

    if date_breakdown_end:
        queryset = queryset.filter(date_breakdown__lte=date_breakdown_end)

    if device_type:
        queryset = queryset.filter(device_instance__device_model__type_id=device_type)

    if malfunction_type:
        queryset = queryset.filter(malfunction_type_id=malfunction_type)

    if performed_by:
        queryset = queryset.filter(performed_by_id=performed_by)


    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="repairs.xlsx"'

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Ремонты"

    # Заголовки столбцов
    columns = [
        "Дата поломки", "Устройство", "Тип неисправности", "Дата устранения", "Выполнил", "Примечание"
    ]
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=1, column=col_num)
        cell.value = column_title

    # Данные
    for row_num, repair in enumerate(queryset, 2):  # Начинаем со второй строки
        worksheet.cell(row=row_num, column=1).value = repair.date_breakdown.strftime('%Y-%m-%d')
        worksheet.cell(row=row_num, column=2).value = str(repair.device_instance)
        worksheet.cell(row=row_num, column=3).value = str(repair.malfunction_type)
        worksheet.cell(row=row_num, column=4).value = repair.date_repair.strftime('%Y-%m-%d') if repair.date_repair else "" # Проверка на None
        worksheet.cell(row=row_num, column=5).value = str(repair.performed_by.FIO)
        worksheet.cell(row=row_num, column=6).value = repair.note

    workbook.save(response)

    return response


def maintenance_list(request):
    maintenances = Maintenance.objects.all().select_related('device_instance', 'device_instance__device_model',
                                                            'performed_by', 'type')
    context = {'maintenances': maintenances}
    return render(request, 'core/maintenance_list.html', context)
