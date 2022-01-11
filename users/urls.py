from django.urls import path

from .views import UserCountries

urlpatterns = [
    path('<slug>', UserCountries.as_view(), name='user-countries'),
]
