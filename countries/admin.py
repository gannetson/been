from django.contrib import admin
# Register your models here.
from django.contrib.admin import register
from django.utils.html import format_html
from django_countries.fields import Country

from .models import UserCountry, UserRegion, Region


@register(UserCountry)
class UserCountryAdmin(admin.ModelAdmin):
    pass


class UserCountryInline(admin.TabularInline):
    model = UserCountry

    readonly_fields = ['flag_image',]
    extra = 0

    @staticmethod
    def flag_image(obj):
        if not obj.country:
            return '-'
        return format_html('<img width=30 src="{}">', obj.flag)


class UserRegionInline(admin.TabularInline):
    model = UserRegion

    readonly_fields = ['flag_image',]
    extra = 0

    @staticmethod
    def flag_image(obj):
        if not obj.region:
            return '-'
        return format_html('<img width=30 src="{}">', obj.flag)


@register(Region)
class RegionAdmin(admin.ModelAdmin):
    model = Region
