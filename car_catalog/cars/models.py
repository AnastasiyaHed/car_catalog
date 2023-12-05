from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class CarAccessory(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarPurchase(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    accessories = models.ManyToManyField('CarAccessory', blank=True, limit_choices_to={'car': models.F('car')})
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} - {self.car.make} {self.car.model}"
