from django.contrib import admin

# Register your models here.
from .models import Customer, Job, CustomerJob


@admin.register(Job)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'dtt_record', 'slug']


# @admin.register(ClientServices)
class ClientServicesAdmin(admin.TabularInline):
    list_display = ['customer', 'job', 'recurrent', 'dtt_start', 'dtt_end', 'dtt_record']
    model = CustomerJob
    extra = 1


@admin.register(Customer)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'dtt_record']
    inlines = [ClientServicesAdmin]
