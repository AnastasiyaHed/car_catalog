from django.urls import path
from .views import car_list, add_car, purchase_car, car_detail, purchase_success

urlpatterns = [
    path('', car_list, name='car_list'),
    path('add/', add_car, name='add_car'),
    path('purchase/<int:car_id>/', purchase_car, name='purchase_car'),
    path('car_detail/<int:car_id>/', car_detail, name='car_detail'),
    path('purchase_success/<int:purchase_id>/', purchase_success, name='purchase_success'),
]