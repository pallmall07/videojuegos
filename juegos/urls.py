from django.urls import path
from . import  views

urlpatterns = [

    path('videojuegos', views.generar_juego)

]


