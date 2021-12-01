from django.urls import path
from noLineales.views import (
    biseccion,
    falsaPosicion,
    puntoFijo,
    secante,
    mabiertos,
    newtonRaphson,
    home_view,    
)

app_name = 'noLineales'
urlpatterns = [
    path('Biseccion', biseccion, name ="Biseccion" ),
    path('Falsa-Posicion',falsaPosicion, name ='Falsa-Posicion'),
    path('Secante', secante, name = 'Secante'),
    path('Newton-Raphson', newtonRaphson, name ='Newton-Raphson'),
    path('Punto-Fijo', puntoFijo, name = "Punto-Fijo"),
    #pa probar
    path('mabiertos',mabiertos, name = "mabiertos"),
    path('home',home_view, name="home_view"),
]

