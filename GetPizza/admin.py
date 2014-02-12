from django.contrib import admin

from GetPizza.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name','login', 'password')
    list_filter = ['name']   

admin.site.register(Customer, CustomerAdmin)
