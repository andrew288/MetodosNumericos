from django.http.response import JsonResponse
from django.shortcuts import render
import json
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
        Sx = Sx + data[i][0]
        Sy = Sy + data[i][1]
        Sxy = round(Sxy + xy[i],4)
        Sx2 = Sx2 + x2[i]
        Sy2 = Sy2 + y2[i]
    
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