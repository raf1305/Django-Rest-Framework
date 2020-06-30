from city.models import City
import sys
import pandas as pd
f=pd.read_csv('city.csv',sep=';',usecols=[1,2,3,4])
for i in range (0,100):
    item=City.objects.create(name=f["Name"][i],countrycode=f["CountryCode"][i],district=f["District"][i],population=int(f["Population"][i]))
