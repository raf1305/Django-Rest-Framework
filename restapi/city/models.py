from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=30)
    countrycode=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    population=models.IntegerField(null=True)

    def __str__(self):
        return self.district