from django.contrib import admin
from .models import UserInfo, Address, Country, Region, City


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    list_display_links = ['full_name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'street_name']
    list_display_links = ['id']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
