from django.shortcuts import render
from sympy import *
from .metodos.Biseccion import metodo_biseccion
from .metodos.FalsaPosicion import metodo_posicion_falsa
from .metodos.PuntoFijo import metodo_punto_fijo
from .metodos.NewtonRapshon import  metodo_newton_raphson
from .metodos.Secante import metodo_secante
from .metodos.Graeffe import metodo_graeffe
from .metodos.Muller import metodo_muller
from .metodos.NewtonRaphsonModificado import metodo_nr_modificado 
from .metodos.bairstow import bairstow




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
        truncate = request.POST["truncate"]
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
        truncate = request.POST["truncate"]
        context =  metodo_posicion_falsa(funcionF, puntoA, puntoB, error, truncate)

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
    return render(request, 'puntoFijo.html', context=context)
    
#Vista para el Newton Raphson
def newtonRaphson(request):
    context = {}
    if request.POST:
        #request
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        errorEstimado =  request.POST["errorEstimado"]
        context = metodo_newton_raphson(funcion, puntoA, errorEstimado)
        
    return render(request, 'newtonRaphson.html', context=context)

#Vista para métodos abiertos.
def mabiertos(request):
    context ={}

    if request.POST:

        #request
        metodo = request.POST["method"]
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        errorEstimado =  request.POST["errorEstimado"]

        if metodo == "puntoFijo":
            context = metodo_punto_fijo(funcion, puntoA,errorEstimado)
        if metodo == "newtonRaphson":
            context = metodo_newton_raphson(funcion, puntoA,errorEstimado)
        if metodo == "secante":
            context = metodo_secante(funcion, puntoA,errorEstimado)
        if metodo == "newtonRaphsonModificado":
            context = metodo_nr_modificado(funcion, puntoA,errorEstimado)
        
    return render(request, 'mabiertos.html', context=context)

#Vista para newtonRaphsonModificado
def newtonRaphsonModificado(request):
    context = {}
    if request.POST:
        #request
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        errorEstimado =  request.POST["errorEstimado"]
        context = metodo_nr_modificado(funcion, puntoA, errorEstimado)
        
    return render(request, 'newtonRaphsonModificado.html', context=context)

#Vista para secante
def secante(request):
    context = {}
    if request.POST:
        #request
        funcion = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        errorEstimado =  request.POST["errorEstimado"]
        context = metodo_secante(funcion, puntoA, errorEstimado )
    return render(request, 'secante.html', context=context)

#Vista de convencionales
def graeffe(request):
    context = {}
    if request.POST:
        c1 = request.POST["coef1"]
        c2 = request.POST["coef2"]
        c3 = request.POST["coef3"]
        c4 = request.POST["coef4"]
        context = metodo_graeffe(c1, c2, c3, c4)
    return render(request, 'graeffe.html', context=context)

def muller(request):
    context = {}
    if request.POST:
        funcionF = request.POST["inputField"]
        puntoA =  request.POST["puntoA"]
        puntoB = request.POST.get("puntoB",False)
        error = request.POST["error"]
        truncate = request.POST["truncate"]
        context = metodo_muller(funcionF, puntoA, puntoB, error, truncate)
    return render(request, 'muller.html', context=context)

def bairstowView(request):
    context = {}
    context['value_error'] = 0.001
    if request.POST:
        expresion = request.POST["expresion"]
        valor_r = request.POST["r"]
        valor_s = request.POST["s"]
        error = request.POST["error"]
        context = bairstow(expresion, float(error), int(valor_r), int(valor_s))
        context['value_error'] = error
        context['expresion'] = expresion
        context['valor_r'] = valor_r
        context['valor_s'] = valor_s
    return render(request, 'bairstow.html', context=context)


