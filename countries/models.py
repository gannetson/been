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
        return f'https://www.worldatlas.com/r/w425/img/flag/{self.country.code.lower()}-flag.jpg'

    def __str__(self):
        return f"Countries for {self.user}"
