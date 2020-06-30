from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .models import City
from .serializers import CitySerializer
# Create your views here.
class CityList(APIView):

    def get(self,request):
        city=City.objects.all()
        serializer=CitySerializer(city,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass
    
class CountryList(APIView):
    def get(self,request,country):
        city=City.objects.all().filter(countrycode=country)
        if not city:
            return HttpResponse(status=404)
        serializer=CitySerializer(city,many=True)
        return JsonResponse(serializer.data,safe=False)    
    def post(self):
        pass