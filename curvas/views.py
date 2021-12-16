from django.http.response import JsonResponse
from django.shortcuts import render
import json
from .metodos.lagrange import lagrange
import math
# Create your views here.


def metodo_minimos_cuadrados(data):
    N = len(data)
    xy = []
    x2 = []
    y2 = []
    Sx = 0
    Sy = 0
    Sxy = 0
    Sx2 = 0
    Sy2 = 0
    m = 0
    b = 0
    c = 0

    for i in range(N):
        
        #agregar valores
        xy.append(round(data[i][0]*data[i][1],4))
        x2.append(round(data[i][0]*data[i][0],4))
        y2.append(round(data[i][1]*data[i][1],4))

        #sumatorias
        Sx = round(Sx + data[i][0],4)
        Sy = round(Sy + data[i][1],4)
        Sxy = round(Sxy + xy[i],4)
        Sx2 = round(Sx2 + x2[i],4)
        Sy2 = round(Sy2 + y2[i],4)
    
    m = round(((N*Sxy)-(Sx*Sy))/((N*Sx2)-(Sx*Sx)),4)
    b = round(((Sy*Sx2)-(Sx*Sxy))/((N*Sx2)-(Sx*Sx)),4)
    c = round(((N*Sxy)-(Sx*Sy))/((((N*Sx2)-(Sx*Sx))**(1/2))*(((N*Sy2)-(Sy*Sy))**(1/2))),4)
    funcion = f'y = {m}x + {b}'

    context = {
        "m":m,
        "b":b,
        "c":c,
        "funcion":funcion,
        "puntos":data,
        "xy":xy,
        "x2":x2,
        "y2":y2,
        "n":N,
        "sx":Sx,
        "sy":Sy,
        "sxy":Sxy,
        "sx2":Sx2,
        "sy2":Sy2,
    }

    return context

def minimos_cuadrados_ajax(request):
    data = json.loads(request.body)
    print(data)
    solucion = metodo_minimos_cuadrados(data)
    return JsonResponse(json.dumps(solucion), safe=False)

def minimos_cuadrados_view(request):
    context = {}
    return render(request, 'minimos-cuadrados.html', context=context)




def metodo_diferencias_divididas(data):
    N = len(data)

    xis = []
    Solucion = []

    for i in range(N):
        xis.append(data[i][0])
        Solucion.append(data[i][1])

    print(Solucion)
    print(xis)
    it = N-1
    it2 = 0
    for i in range(N-1):
        for j in range(it):
            Solucion.append((Solucion[it2+1]-Solucion[it2])/(xis[j+i+1]-xis[j]))
            if j==N-2-i:
                it2=it2+2
            else :
                it2=it2+1
        it=it-1
        print('\n')  
    it = N
    it2 = 0
    for i in range(N):
        for j in range(it):
            print(Solucion[it2])
            it2=it2+1
            
        it=it-1
        print('\n')  
    
    strFuncion = f'{Solucion[0]} + '
    strXs = ""
    it = N
    it2 = 1
    for i in range(N):
        if i >=1:
            strXs = strXs + f'(x-{xis[i-1]})'
        for j in range(it):
            if j==0 and i>=1:
                strFuncion =  strFuncion+ f'{Solucion[it2-1]}*{strXs} + '
            it2=it2+1
            
        it=it-1

    strFuncion = strFuncion[:-2]

    

    context = {
        "data" : Solucion,
        "xis" : xis,
        "n" : N,
        "funcion" : strFuncion,
    }
    
    return context


def diferencias_divididas_ajax(request):
    data = json.loads(request.body)
    print(data)
    solucion = metodo_diferencias_divididas(data)
    return JsonResponse(json.dumps(solucion), safe=False)


def diferencias_divididas_view(request):
    context = {}
    return render(request, 'diferencias-divididas.html', context=context)


def lagrangeViewAjax(request):
    data = json.loads(request.body.decode("utf-8"))
    matriX = data['X']
    matriY = data['Y']
    print(matriX)
    print(matriY)
    solucion = lagrange(matriX, matriY)
    return JsonResponse(solucion, safe=False)

def lagrangeView(request):
    context = {}

    return render(request, 'lagrange.html', context=context)




def metodo_diferencias_finitas(data):
    N = len(data)

    xis = []
    Solucion2 = []

    for i in range(N):
        xis.append((data[i][0]))
        Solucion2.append(data[i][1])

    print(Solucion2)
    print(xis)
    it = N-1
    it2 = 0
    for i in range(N-1):
        for j in range(it):
            Solucion2.append((Solucion2[it2+1]-Solucion2[it2]))
            if j==N-2-i:
                it2=it2+2
            else :
                it2=it2+1
        it=it-1
        print('\n')  
    it = N
    it2 = 0
    for i in range(N):
        for j in range(it):
            print(Solucion2[it2])
            it2=it2+1
            
        it=it-1
        print('\n')  
    
    strFuncion = f'{Solucion2[0]} + ' 
    strXs = ""
    it = N
    it2 = 1
    for i in range(N):
        if i >=1:
            strXs = strXs + f'(x-{xis[i-1]})'
        for j in range(it):
            if j==0 and i>=1:
                strFuncion =  strFuncion+ f'{Solucion2[it2-1]/((math.factorial(i)*math.pow(xis[j+1]-xis[j],i)))}*{strXs} + '
            it2=it2+1
            
        it=it-1

    strFuncion = strFuncion[:-2]
    context = {
        "data" : Solucion2,
        "xis" : xis,
        "n" : N,
        "funcion" : strFuncion,
    }
    
    return context


def diferencias_finitas_ajax(request):
    data = json.loads(request.body)
    print(data)
    solucion = metodo_diferencias_finitas(data)
    return JsonResponse(json.dumps(solucion), safe=False)


def diferencias_finitas_view(request):
    context = {}
    return render(request, 'diferencias-finitas.html', context=context)

