from django.urls import path
from algebraicas.views import (Gauss_seidel, Gauss_seidelRelax_ajax, Gauss_seidelRelax, Jacobi, Jacobi_ajax,
    gauss_jordan_ajax,
    gauss_jordan_view,
    gauss_seidel_ajax,
    eliminacion_gauss_view,
    eliminacion_gauss_ajax,
    Jacobi,
    Jacobi_ajax,
)

app_name = 'algebraicas'
urlpatterns = [
    path('Gauss_Jordan', gauss_jordan_view, name="gauss_jordan_view"),
    path('Gauss_Jordan_Ajax', gauss_jordan_ajax, name="gauss_jordan_ajax"),
    path('Gauss_Seidel', Gauss_seidel, name ="Gauss-seidel" ),
    path('Gauss_Seidel_Ajax', gauss_seidel_ajax, name="gauss_seidel_ajax"),
    path('Gauss_Seidel_Relax',Gauss_seidelRelax,name="Gauss_seidelRelax"),
    path('Gauss_SeidelRelax_Ajax',Gauss_seidelRelax_ajax,name="Gauss_seidelRelax_ajax"),
    path('Gauss', eliminacion_gauss_view, name="gauss-eliminacion"),
    path('Gauss-Ajax', eliminacion_gauss_ajax, name="gauss-eliminacion-ajax"),
    path('Jacobi', Jacobi, name="Jacobi"),
    path('Jacobi_Ajax', Jacobi_ajax, name="Jacobi_Ajax"),
]