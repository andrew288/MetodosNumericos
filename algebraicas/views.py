from django.http.response import JsonResponse
from django.shortcuts import render
from .metodos.GaussSeidel import metodo_gauss_seidel
from .metodos.GaussSeidelRelax import metodo_gauss_seidelRelax
from .metodos.GaussJordan import metodo_gauss_jordan
from .metodos.Jacobi import metodo_jacobi
from .metodos.eliminacionGauss import eliminacionGauss
from sympy import *
import numpy as np

import json

# Create your views here.
def gauss_jordan_ajax(request):
    
    data = json.loads(request.body)
    solucion = metodo_gauss_jordan(data)
    
    return JsonResponse(json.dumps(solucion), safe=False)

def gauss_jordan_view(request):
    context = {}
    return render(request, 'gauss_jordan.html', context=context)
#----------GAUS SEIDEL-----------------
def gauss_seidel_ajax(request):
    data = json.loads(request.body)
    solucion = metodo_gauss_seidel(data["Matrix"], data["Error"])

    return JsonResponse(json.dumps(solucion), safe=False)
def Gauss_seidel(request):
    context = {}
    return render(request, 'gauss-seidel.html', context)
#---------GAUS SEIDEL RELAX-------------------
def Gauss_seidelRelax_ajax(request):
    data = json.loads(request.body)
    solucion = metodo_gauss_seidelRelax(data["Matrix"], data["Error"],data["Peso"])
    return JsonResponse(json.dumps(solucion), safe=False)

def Gauss_seidelRelax(request):
    context = {}
    return render(request,'gauss-seidelRelax.html',context)

def eliminacion_gauss_view(request):
    context = {}

    return render(request,'eliminacion-gauss.html', context)

def eliminacion_gauss_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    matriz = data['matriz']
    solucion = eliminacionGauss(matriz)
    return JsonResponse(solucion, safe=False)

def Jacobi(request):
    context = {}
    return render(request,'jacobi.html',context)

def Jacobi_ajax(request):
    data = json.loads(request.body)
    solucion = metodo_jacobi(data["Matrix"], data["Error"])
    return JsonResponse(json.dumps(solucion), safe=False)
