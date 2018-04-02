from django.contrib import admin
from .models import Device, Diagnosis, Patient, PatientInstance

# Register your models here.

#Register new device
class DeviceAdmin(admin.ModelAdmin):

    list_display = ('number_id', 'device_name', 'clinic_name', 'date_of_purchase')
    fields = ['number_id', 'device_name', 'clinic_name', ('date_of_purchase')]

admin.site.register(Device, DeviceAdmin)
admin.site.register(Diagnosis)

class PatientInstanceInline(admin.TabularInline):
    model = PatientInstance


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'device', 'display_diagnosis')
    inlines = [PatientInstanceInline]


@admin.register(PatientInstance)
class PatientInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'discharge_time')

    fieldsets = (
        (None, {
            'fields': ('patient', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'discharge_time')
        })

    )