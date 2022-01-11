import django_countries.data
import glob
import os

from django_countries.base import CountriesBase

try:
    from django.utils.translation import gettext_lazy as _
except ImportError:  # pragma: no cover
    # Allows this module to be executed without Django installed.
    def _(x):
        return x


django_countries.data.COUNTRIES["XK"] = _("Kosovo")


