from django.contrib import admin
from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product)
