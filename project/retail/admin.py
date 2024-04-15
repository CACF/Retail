from django.contrib import admin
from .models import Customer,Supplier,Distribution_center,Employee,Order,Product
# Register your models here.
@admin.register(Customer)
class customer_page(admin.ModelAdmin):
    list_display = ["customer_id", "name", "contact_information", "address"]

@admin.register(Order)
class order_page(admin.ModelAdmin):
    list_display = ["order_id", "name", "date", "status","customer_id"]
    list_filter = ('status',)
    search_fields = ('name', 'status', 'customer_id__name') 

@admin.register(Supplier)
class supplier_page(admin.ModelAdmin):
    list_display = ["supplier_id", "name", "contact_information", "address"]


@admin.register(Product)
class product_page(admin.ModelAdmin):
    list_display = ["product_id", "name", "brand", "flavour","price","quantity","expiry_date","product_id"]
    list_filter = ('brand', 'flavour')
    search_fields = ('name', 'brand', 'flavour')
    filter_horizontal = ('order',)


@admin.register(Distribution_center)
class distribution_page(admin.ModelAdmin):
    list_display = ["center_id","capacity","address"]


@admin.register(Employee)
class employee_page(admin.ModelAdmin):
    list_display = ["employee_id","name","contact_information","address","center_id"]