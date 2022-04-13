from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.car_detail),
    path('', views.cars_list),
]