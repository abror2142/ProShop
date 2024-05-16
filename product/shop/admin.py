from django.contrib import admin
from .models import Product, Category, Measurement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'added_at']
    list_display_links = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'symbol', 'is_decimal_measurable']
    list_display_links = ['full_name']
    list_editable = ['symbol', 'is_decimal_measurable']