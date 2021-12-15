from django.urls import path
from algebraicas.views import (Gauss_seidel, Gauss_seidelRelax_ajax, Gauss_seidelRelax,
    gauss_jordan_ajax,
    gauss_jordan_view,
    gauss_seidel_ajax,
   
)

app_name = 'algebraicas'
urlpatterns = [
    #path('', , name ="" ),
    path('Gauss_Jordan', gauss_jordan_view, name="gauss_jordan_view"),
    path('Gauss_Jordan_Ajax', gauss_jordan_ajax, name="gauss_jordan_ajax"),
    path('Gauss_Seidel', Gauss_seidel, name ="Gauss-seidel" ),
    path('Gauss_Seidel_Ajax', gauss_seidel_ajax, name="gauss_seidel_ajax"),
    path('Gauss_SeidelRelax',Gauss_seidelRelax,name="Gauss_seidelRelax"),
    path('Gauss_SeidelRelax_Ajax',Gauss_seidelRelax_ajax,name="Gauss_seidelRelax_ajax"),
    
]