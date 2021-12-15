from django.http.response import JsonResponse
from django.shortcuts import render
from .metodos.GaussSeidel import metodo_gauss_seidel
from sympy import *
import numpy as np
import json

# Create your views here.


def mostrar_matriz(data):
    for i in range(len(data)):
        for j in range(len(data)+1):
            print(data[i][j], end=" ")
        print()

def metodo_gauss_jordan(data):
    # i numero de filas j numero de columnas
    a = data
    n = len(a)
    x = np.zeros(n)
    solucion = []

    mostrar_matriz(a)
    for i in range(n):
        if a[i][i] == 0.0:
            print("No se puede dividir entre 0")

        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]

                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
                print()
                mostrar_matriz(a)

    # Obtener solucion
    for i in range(n):
        x[i] = a[i][n] / a[i][i]

    # Mostrar solucion
    # print('\nRequired solution is: ')
    # for i in range(n):
    #     print('X%d = %0.2f' % (i, x[i]), end='\t')

    for i in x:
        solucion.append(i)

    return solucion


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
