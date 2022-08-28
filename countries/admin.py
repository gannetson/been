from django.contrib import admin
# Register your models here.
from django.contrib.admin import register
from django.utils.html import format_html

from .models import UserCountry


@register(UserCountry)
class UserCountryAdmin(admin.ModelAdmin):
    pass


class UserCountryInline(admin.TabularInline):
    model = UserCountry

    readonly_fields = ['flag_image',]

    @staticmethod
    def flag_image(obj):
        if not obj.country:
            return '-'
        return format_html('<img width=30 src="https://www.worldatlas.com/r/w425/img/flag/{}-flag.jpg">', obj.country.code.lower())
