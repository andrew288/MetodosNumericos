from django.http.response import JsonResponse
from django.shortcuts import render
from .metodos.GaussSeidel import metodo_gauss_seidel
from .metodos.GaussJordan import metodo_gauss_jordan

import json

# Create your views here.
def gauss_jordan_ajax(request):
     
     data = json.loads(request.body)
     solucion = metodo_gauss_jordan(data)
     
     return JsonResponse(json.dumps(solucion), safe=False)
#Vista para gauss seidel
def gauss_seidel_ajax(request):
    data = json.loads(request.body)
    print(data["Matrix"])
    solucion = metodo_gauss_seidel(data["Matrix"], data["Error"])

    return JsonResponse(json.dumps(solucion), safe=False)

def Gauss_seidel(request):
    context = {}
    return render(request, 'gauss-seidel.html', context)
    
def gauss_jordan_view(request):
    context = {}
    return render(request, 'gauss_jordan.html', context=context)
