from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView

# Create your views here.
from django.views.generic import DetailView

from users.serializers import UserSerializer


class UserCountries(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'user_countries.html'


class UserDetailApiView(RetrieveUpdateAPIView):
    queryset = User.objects
    slug_field = 'username'
    lookup_field = 'username'
    model = User
    serializer_class = UserSerializer