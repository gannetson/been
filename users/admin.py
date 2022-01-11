from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from django.contrib.auth.models import User

from countries.admin import UserCountryInline

admin.site.unregister(User)

@register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (UserCountryInline,)
