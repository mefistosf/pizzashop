from django.contrib import admin
from getpizza.models import Pizza
from getpizza.models import Customer

admin.site.register(Pizza)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'login', 'password')
    list_filter = ['name']

admin.site.register(Customer, CustomerAdmin)

