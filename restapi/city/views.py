from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .models import City
from .serializers import CitySerializer,CategorySerializer
from django.db.models import Q
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
        city=City.objects.all().filter(countrycode__iexact=country).order_by('name')
        if not city:
            return HttpResponse(status=404)
        serializer=CitySerializer(city,many=True)
        return JsonResponse(serializer.data,safe=False)    
    def post(self):
        pass
class CityList(APIView):
    def get(self,request,country,city):
        print(country,city)
        city=City.objects.filter(countrycode__iexact=country).filter(name__iexact=city)
        print(city)
        if not city:
            return HttpResponse(status=404)
        serializer=CitySerializer(city,many=True)
        return JsonResponse(serializer.data,safe=False)    
    def post(self):
        pass
class CategoryList(APIView):
    def get(self,request):
        city=City.objects.all().order_by('countrycode')
        print(city)
        if not city:
            return HttpResponse(status=404)
        serializer=CategorySerializer(city,many=True)
        response = JsonResponse(serializer.data,safe=False) 
        return response
    def post(self):
        pass