from django.urls import path
from city import views

urlpatterns = [
    path('', views.CityList.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('<str:country>/', views.CountryList.as_view()),
    path('<str:country>/<str:city>/', views.CityList.as_view()),
    # path('', views.CountryList.as_view()),
]