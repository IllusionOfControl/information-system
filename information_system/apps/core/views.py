from django.shortcuts import render

from information_system.apps.core.models import Department, DeviceModel


def department_list(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'core/department_list.html', context)


def device_list(request):
    devices = DeviceModel.objects.all()
    context = {'devices': devices}
    return render(request, 'core/device_list.html', context)

