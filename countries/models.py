from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from django.db.models import CASCADE
from django.utils.timezone import now
from django_countries.fields import CountryField
from .monkey import *


class UserCountry(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, related_name='countries', on_delete=CASCADE)
    country = CountryField()
    year = models.IntegerField(default=now().year)
    foto = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'User country'
        verbose_name_plural  = 'User countries'
        ordering = ['year']

    @property
    def flag(self):
        return f'https://flagcdn.com/{self.country.code.lower()}.svg'

    @property
    def name(self):
        return self.country.name

    def __str__(self):
        return f"Countries for {self.user}"


class Region(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserRegion(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='regions', on_delete=CASCADE)
    region = models.ForeignKey(Region, related_name='users', on_delete=CASCADE)
    year = models.IntegerField(default=now().year)
    foto = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'User extra regions'
        verbose_name_plural  = 'User extra regions'
        ordering = ['year']

    @property
    def flag(self):
        return f'https://flagcdn.com/{self.region.code.lower()}.svg'

    @property
    def name(self):
        return self.region.name

    def __str__(self):
        return f"Extra regions for {self.user}"
