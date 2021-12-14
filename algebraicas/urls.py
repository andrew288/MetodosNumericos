from django.urls import path
from algebraicas.views import (Gauss_seidel)
app_name = 'algebraicas'
urlpatterns = [
    path('Gauss-seidel', Gauss_seidel, name ="Gauss-seidel" ),
]