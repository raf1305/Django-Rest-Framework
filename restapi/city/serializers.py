from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        # field=['ticker','volume']
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        # field=['ticker','volume']
        fields=['countrycode','name']