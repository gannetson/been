from countries.models import UserCountry, UserRegion
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User



class UserCountrySerializer(ModelSerializer):

    class Meta:
        model = UserCountry
        fields = ['id', 'country', 'year', 'name', 'flag']


class UserRegionSerializer(ModelSerializer):

    class Meta:
        model = UserRegion
        fields = ['id', 'region', 'year', 'name', 'flag']


class UserSerializer(ModelSerializer):
    countries = UserCountrySerializer(many=True)
    regions = UserRegionSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'countries', 'regions']