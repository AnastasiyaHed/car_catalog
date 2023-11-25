# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.car_list, name='car_list'),
#
# ]

from django.urls import path
from .views import CarListView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
]