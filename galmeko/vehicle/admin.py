from django.contrib import admin
from .forms import CustomVehicleCreationForm
from django.utils.html import format_html
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from vehicle.models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    form = CustomVehicleCreationForm
    model = Vehicle
    list_display = ('vehicle_no','chassis_no','status')
    list_filter = ('status',)
    list_per_page = 5  

    fieldsets = (
        (None, {'fields': ('vehicle_no','chassis_no','status')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('vehicle_no','chassis_no','status')}
        ),
    )
    search_fields = ('company_name',)
    ordering = ('-id',)


    def save_vehicle(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

admin_site.register(Vehicle,VehicleAdmin)
