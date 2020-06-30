from django.urls import path
from city import views

urlpatterns = [
    path('', views.CityList.as_view()),
    path('<str:country>/', views.CountryList.as_view()),
]