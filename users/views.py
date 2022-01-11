from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import DetailView


class UserCountries(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'user_countries.html'
