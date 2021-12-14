from django.urls import path
#from algebraicas.views import()
from algebraicas.views import (
    gauss_jordan_ajax,
    gauss_jordan_view,
)


app_name = 'algebraicas'
urlpatterns = [
    #path('', , name ="" ),
    path('Gauss_Jordan', gauss_jordan_view, name="gauss_jordan_view"),
    path('Gauss_Jordan_Ajax', gauss_jordan_ajax, name="gauss_jordan_ajax")
]