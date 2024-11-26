from django import forms

from information_system.apps.core.models import Repair, Maintenance, User, DeviceInstance


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['date_breakdown', 'device_instance', 'malfunction_type', 'date_repair', 'performed_by', 'note']
        widgets = {
            'date_breakdown': forms.DateInput(attrs={'type': 'date'}),
            'date_repair': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3})
        }



class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'device_instance', 'type', 'performed_by', 'note']
        widgets = {
            "date": forms.DateInput(attrs={'type': 'date'}),
            "note": forms.Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        user: User | None = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            if user.role == 'master':
                self.fields['performed_by'].queryset = User.objects.filter(pk=user.pk) # Только текущий пользователь
            elif user.role == 'administrator':
                self.fields['performed_by'].queryset = User.objects.filter(role__in=['master', 'administrator'])
            # Ограничиваем выбор устройств только теми, что относятся к отделению пользователя, если он не администратор
            if user.role != 'administrator':
                self.fields['device'].queryset = DeviceInstance.objects.all()