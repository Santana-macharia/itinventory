#admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect



from .models import Import, Report


class ImportAdmin(admin.ModelAdmin):
    # list_display = ('get_display_field', 'centre', 'department', 'hardware', 'system_model', 'processor', 'ram_gb', 'hdd_gb', 'serial_number', 'assignee_first_name', 'assignee_last_name', 'assignee_email_address', 'device_condition', 'status', 'date')
    list_display = ('centre', 'department', 'hardware', 'system_model', 'processor', 'ram_gb', 'hdd_gb', 'serial_number', 'assignee_first_name', 'assignee_last_name', 'assignee_email_address', 'device_condition', 'status', 'date')
    search_fields = ['centre', 'department', 'hardware', 'system_model', 'processor', 'ram_gb', 'hdd_gb', 'serial_number', 'assignee_first_name', 'assignee_last_name', 'assignee_email_address', 'device_condition', 'status', 'date']

    def get_display_field(self, obj):
        return obj.display_field

    get_display_field.short_description = 'Display Field'
  

admin.site.register(Import, ImportAdmin)


class ReportAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        displaycsv_url = reverse('displaycsv_template')  # Updated reverse URL lookup
        return redirect(displaycsv_url)
    


    def changelist_view(self, request, extra_context=None):
        redirect_url = reverse('displaycsv_template')
        return redirect(redirect_url)

admin.site.register(Report, ReportAdmin)



