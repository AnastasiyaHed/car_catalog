from .models import Car, CarPurchase, CarAccessory
from .forms import CarForm, CarPurchaseForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import logging
from django.shortcuts import render, redirect
from .models import CarPurchase


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

# @login_required
# def purchase_car(request, car_id):
#     car = get_object_or_404(Car, pk=car_id)
#
#     if request.method == 'POST':
#         form = CarPurchaseForm(request.POST)
#         if form.is_valid():
#             purchase = form.save(commit=False)
#             purchase.car = car
#             purchase.save()
#             return render(request, 'purchase_success.html', {'car': car, 'purchase': purchase})
#     else:
#         form = CarPurchaseForm()
#
#     return render(request, 'cars/purchase_car.html', {'car': car, 'form': form})



def purchase_car(request, car_id):
    if request.method == 'POST':
        form = CarPurchaseForm(request.POST)
        if form.is_valid():
            # Предполагая, что у вас есть доступ к объекту машины (car) по car_id
            car = Car.objects.get(id=car_id)

            # Сохраняем покупку с каким-то значением для buyer (в данном случае, строкой)
            purchase = form.save(commit=False)
            purchase.car = car
            purchase.buyer = "Anonymous"  # Можете использовать любое значение для представления "незарегистрированного" пользователя
            purchase.save()

            # Далее можете добавить логику редиректа или другие действия
            return redirect('purchase_success')
    else:
        form = CarPurchaseForm()

    return render(request, 'cars/purchase_car.html', {'form': form})


def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    accessories = CarAccessory.objects.filter(car=car)
    return render(request, 'cars/car_detail.html', {'car': car, 'accessories': accessories})


def purchase_success(request, purchase_id):
    purchase = get_object_or_404(CarPurchase, pk=purchase_id)
    return render(request, 'cars/purchase_success.html', {'purchase': purchase})



logger = logging.getLogger(__name__)



