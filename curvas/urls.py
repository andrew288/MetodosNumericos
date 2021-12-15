from django.urls import path
#from curvas.views import()

from curvas.views import (
    minimos_cuadrados_ajax,
    minimos_cuadrados_view,
    diferencias_divididas_view,
    diferencias_divididas_ajax
)

app_name = 'curvas'
urlpatterns = [
    #path('', , name ="" ),
    path('Minimos_Cuadrados', minimos_cuadrados_view, name="minimos_cuadrados"),
    path('Minimos_Cuadrados_Ajax', minimos_cuadrados_ajax, name="minimos_cuadrados_ajax"),
    path('Diferencias_Divididas', diferencias_divididas_view, name="diferencias_divididas"),
    path('Diferencias_Divididas_Ajax', diferencias_divididas_ajax, name="diferencias_divididas_ajax"),
]