from django.shortcuts import render, get_object_or_404

from information_system.apps.core.models import Department, DeviceModel, DeviceInstance, DeviceType


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
        device_instances = DeviceInstance.objects.filter(device_model__type=selected_device_type).select_related('device_model')

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
