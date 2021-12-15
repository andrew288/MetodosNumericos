from django.http.response import JsonResponse
from django.shortcuts import render
import json
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
        xy.append(data[i][0]*data[i][1])
        x2.append(data[i][0]*data[i][0])
        y2.append(data[i][1]*data[i][1])

        #sumatorias
        Sx = Sx + data[i][0]
        Sy = Sy + data[i][1]
        Sxy = Sxy + xy[i]
        Sx2 = Sx2 + x2[i]
        Sy2 = Sy2 + y2[i]
    
    m = ((N*Sxy)-(Sx*Sy))/((N*Sx2)-(Sx*Sx))
    b = ((Sy*Sx2)-(Sx*Sxy))/((N*Sx2)-(Sx*Sx))
    c = ((N*Sxy)-(Sx*Sy))/((((N*Sx2)-(Sx*Sx))**(1/2))*(((N*Sy2)-(Sy*Sy))**(1/2)))
    funcion = f'y = {m}x + {b}'

    context = {
        "m":m,
        "b":b,
        "c":c,
        "funcion":funcion,
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
    
    strFuncion = ""
    strXs = ""
    it = N
    it2 = 0
    for i in range(N):
        strXs = strXs + f'(x-{xis[i]})'
        for j in range(it):
            if j==0:
                strFuncion =  strFuncion+ f'{Solucion[it2]}*{strXs} + '
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

