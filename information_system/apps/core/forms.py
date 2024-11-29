from django import forms

from information_system.apps.core.models import Repair, Maintenance, User


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['date_breakdown', 'device_instance', 'malfunction_type', 'date_repair', 'performed_by', 'note']
        widgets = {
            'date_breakdown': forms.DateInput(attrs={'type': 'date'}),
            'date_repair': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        user: User | None = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            if user.role == 'master':
                self.fields['performed_by'].queryset = User.objects.filter(pk=user.pk)

            elif user.role == 'administrator':
                self.fields['performed_by'].queryset = User.objects.filter(role__in=['master'])

    def clean_performed_by(self):
        performed_by = self.cleaned_data['performed_by']
        user: User | None = getattr(self, 'user', None)

        if user and user.role == 'master' and performed_by != user:
            raise forms.ValidationError("Мастер может выбрать только себя в качестве исполнителя.")

        return performed_by


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
                self.fields['performed_by'].queryset = User.objects.filter(pk=user.pk)
            elif user.role == 'administrator':
                self.fields['performed_by'].queryset = User.objects.filter(role__in=['master'])

    def clean_performed_by(self):
        performed_by = self.cleaned_data['performed_by']
        user: User | None = getattr(self, 'user', None)

        if user and user.role == 'master' and performed_by != user:
            raise forms.ValidationError("Мастер может выбрать только себя в качестве исполнителя.")

        return performed_by
