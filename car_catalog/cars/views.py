# from django.shortcuts import render
# from .models import Car
#
# def car_list(request):
#     cars = Car.objects.all()
#     return render(request, 'cars/car_list.html', {'cars': cars})

from django.views.generic import ListView
from .models import Car

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'