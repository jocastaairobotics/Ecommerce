from django.contrib import admin
from .models import ProductCategory, Product, Invoice


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'pricing']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'products', 'totals']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
