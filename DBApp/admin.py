from django.contrib import admin
from .models import Product
# Register your models here.
class PDAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Name', 'Cost', 'Mft', 'Exp']
admin.site.register(Product, PDAdmin)

