from django.shortcuts import render 
from sympy import *
from .metodos.Biseccion import metodo_biseccion
from .metodos.FalsaPosicion import metodo_posicion_falsa
from .metodos.PuntoFijo import metodo_punto_fijo
from .metodos.NewtonRapshon import  metodo_newton_raphson
from .metodos.Secante import metodo_secante

def home_view(request):

    context ={}

    if request.POST:

        #request
        metodo = request.POST["method"]
        funcionF = request.POST["inputField"]
        funcionG = request.POST.get("funcionG",False)
        puntoA =  request.POST["puntoA"]
        puntoB = request.POST.get("puntoB",False)
        error = request.POST["error"]
        truncate = request.POST["truncate"]

        if metodo == "biseccion":
            context = metodo_biseccion(funcionF, puntoA, puntoB, error, truncate)
        if metodo == "falsaPosicion":
            context =  metodo_posicion_falsa(funcionF, puntoA, puntoB, error, truncate)
        if metodo == "puntoFijo":
            context = metodo_punto_fijo(funcionF, funcionG, puntoA, error,truncate)
        
    return render(request, 'home_view.html', context=context)
    
#Vista para método bisección
def biseccion(request):
    context ={}

    if request.POST:
        #request
        funcionF = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        puntoB = request.POST.get("puntoB",False)
        error = request.POST["error"]
        truncate = 0
        context = metodo_biseccion(funcionF, puntoA, puntoB, error, truncate)  
    return render(request, 'biseccion.html', context=context)
    
#Vista para el falsa posición
def falsaPosicion(request):
    context ={}

    if request.POST:
        #request
        funcionF = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        puntoB = request.POST.get("puntoB",False)
        error = request.POST["error"]
        context =  metodo_posicion_falsa(funcionF, puntoA, puntoB, error)

    return render(request, 'FalsaPosicion.html', context=context)

#Vista para punto fijo
def puntoFijo(request):
    context = {}

    if request.POST:
        #request
        funcionF = request.POST["inputField"]
        funcionG = request.POST.get("funcionG",False)
        puntoA =  request.POST["puntoA"]
        error = request.POST["error"]
        truncate = request.POST["truncate"]
        context = metodo_punto_fijo(funcionF, funcionG, puntoA, error, truncate)
    return render(request, 'PuntoFijo.html', context=context)
    
#Vista para el Newton Raphson
def newtonRaphson(request):
    context = {}
    if request.POST:
        #request
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        context = metodo_newton_raphson(funcion, puntoA)
        
    return render(request, 'newtonRaphson.html', context=context)

#Vista para métodos abiertos.
def mabiertos(request):
    context ={}

    if request.POST:

        #request
        metodo = request.POST["method"]
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]

        if metodo == "puntoFijo":
            context = metodo_punto_fijo(funcion, puntoA)
        if metodo == "newtonRaphson":
            context = metodo_newton_raphson(funcion, puntoA)
        if metodo == "secante":
            context = metodo_secante(funcion, puntoA)
        
    return render(request, 'mabiertos.html', context=context)

#Vista para secante
def secante(request):
    context = {}
    if request.POST:
        #request
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        context = metodo_secante(funcion, puntoA)
    return render(request, 'secante.html', context=context)