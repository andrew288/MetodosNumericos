from django.shortcuts import render 
from sympy import *
from math import sqrt
from math import pow
from random import randint

def llenar_matriz(n):
    matriz = []

    for r in range(n + 1):
        fila = []

        for c in range(n):
            fila.append(randint(1,10))
        
        matriz.append(fila)
    
    return matriz

def metodo_gauss_jordan():
    #i numero de filas j numero de columnas
    n=3
    m=4
    a = llenar_matriz(n)

    for i in range(n):
        for j in range(n):
            print(a[i][j])
    # for j in range(0,n-1):
    #     for i in range(n-1,0,-1):



