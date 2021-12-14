from django.shortcuts import render 
from sympy import *
from math import sqrt
from math import pow
# Create your views here.

#Metodos cerrados

def metodo_posicion_falsa(express,puntoA,puntoB, errorEstimado, truncate):
    print("Metodo Falsa Posicion")
    #declaracion de variables
    x = symbols('x')
    #variables necesarias
    str_expr = ""
    count = 0
    itr = 0
    xi = []
    xd = []
    xr = []
    fxi = []
    fxd = []
    fxr = []
    err = []
    error = 0
    
    #parse funcion ingresada
    str_expr = express
    expr= sympify(str_expr, evaluate=False)
    f = lambdify(x,expr)

    #asignacion de puntos iniciales
    xi.append(float(puntoA))
    xd.append(float(puntoB))

    #iteraciones
    while(count<100):
        fxi.append(f(xi[count]))
        fxd.append(f(xd[count]))
        xr.append(xd[count]-((f(xd[count])*(xi[count]-xd[count]))/(f(xi[count])-f(xd[count]))))
        fxr.append(f(xr[count]))
        if( (fxr[count]>0 and fxi[count]>0) or (fxr[count]<0 and fxi[count]<0)):
            xi.append(xr[count])
            xd.append(xd[count])
        else:
            xi.append(xi[count])
            xd.append(xr[count])
        
        if(count>0):
            error = abs((xr[count]-xr[count-1])/xr[count])
            err.append(error)
            if(error == 0 or error <= float(errorEstimado)):
                itr = count + 1
                count = 100
        else:
            err.append(100)

        count=count+1

    #pasamos nuestros valores
    context = {
        "metodo":"posicionFalsa",
        "count":range(itr),
        "nCate":range(7),
        "cate":["xi","xd","xr","f(xi)","f(xd)","f(xr)","Error"],
        "xi":xi,
        "xd":xd,
        "xr":xr,
        "fxi":fxi,
        "fxd":fxd,
        "fxr":fxr,
        "err":err,
    }
    print(context)

    return context

def metodo_biseccion(express,puntoA,puntoB, errorEstimado, truncate):
    print("Metodo Biseccion")
    x = symbols('x')
    str_expr = ""
    count = 0
    itr = 0
    xi = []
    xd = []
    xr = []
    fxi = []
    fxd = []
    fxr = []
    err = []

    error = 0
    #parse funcion ingresada
    str_expr = express
    expr= sympify(str_expr, evaluate=False)
    f = lambdify(x,expr)
    #puntos iniciales
    xi.append(float(puntoA))
    xd.append(float(puntoB))

    while(count<100):
        xr.append((xi[count]+xd[count])/2)
        fxi.append(f(xi[count]))
        fxd.append(f(xd[count]))
        fxr.append(f(xr[count]))
        if( (fxr[count]>0 and fxi[count]>0) or (fxr[count]<0 and fxi[count]<0)):
            xi.append(xr[count])
            xd.append(xd[count])
        else:
            xi.append(xi[count])
            xd.append(xr[count])
        
        if(count>0):
            error = abs((xr[count]-xr[count-1])/xr[count])
            err.append(error)
            if(error < float(errorEstimado) or error == 0):
                itr = count + 1
                count = 100
        else:
            err.append(100)

        count=count+1

    context = {
        "metodo":"biseccion",
        "count":range(itr),
        "nCate":range(7),
        "cate":["xi","xd","xr","f(xi)","f(xd)","f(xr)","Error"],
        "xi":xi,
        "xd":xd,
        "xr":xr,
        "fxi":fxi,
        "fxd":fxd,
        "fxr":fxr,
        "err":err,
    }

    return context

def metodo_puntoFijo(express, funcionG, puntoA, errorEstimado, truncate):
    print("Metodo Punto Fijo")
    x = symbols('x')
    count = 0
    itr = 0
    xi = []
    gx = []
    fx = []
    err = []
    error = 0
    str_exprF = express
    exprF = sympify(str_exprF, evaluate=False)
    print(exprF)
    exprG = sympify(funcionG, evaluate=False)
    print(exprG)
    #funciones
    f = lambdify(x,exprF)
    g = lambdify(x,exprG)

    xi.append(float(puntoA))
    while(count < 100):
        gx.append(g(xi[count]))
        fx.append(abs(f(xi[count])))

        if(count > 0):
                error = abs((xi[count]-xi[count-1])/xi[count])
                err.append(error)
        else:
            err.append(100)

        if(fx[count] > float(errorEstimado)):
            xi.append(gx[count])

            count = count + 1
        
        else:
            itr = count + 1
            count = 100
    
    context = {
        "metodo":"puntoFijo",
        "count":range(itr),
        "nCate":range(4),
        "cate":["xi","|f(x)|","g(x)","Error"],
        "xi":xi,
        "fx":fx,
        "gx":gx,
        "err":err,
    }
    print("xi: ",xi)
    print("g(x): ",gx)
    print("f(x): ",fx)
    print("Err: ", err)

    return context

#metodo de Muller

def metodo_muller(express,puntoA,puntoB, errorEstimado, truncate):
    print("Metodo de Muller")
    #simbolos a utilizar
    x = symbols('x')
    #estructuras utilizadas
    count = 0
    itr = 0
    x0 = []
    x1 = []
    x2 = []
    fx0 = []
    fx1 = []
    fx2 = []
    h0 = []
    h1 = []
    d0 = []
    d1 = []
    a = []
    b = []
    c = []
    x3 = []
    fx3 = []
    err = []
    discriminante = 0
    denominador = 0

    #ahora definimos nuestras formulas
    exprF = sympify(express, evaluate=False)
    print("Funcion F: ",exprF)
    f = lambdify(x,exprF)

    #ahora agregamos nuestros puntos iniciales
    x0.append(float(puntoA))
    x1.append(float(puntoB))
    x2.append((x0[count]+x1[count])/2)

    while(count<100):

        print("Valor de x0: ",x0[count])
        print("Valor de x1: ",x1[count])
        print("Valor de x2: ",x2[count])
        fx0.append(f(x0[count]))
        print("Valor de fx0: ",fx0[count])
        fx1.append(f(x1[count]))
        print("Valor de fx1: ",fx1[count])
        fx2.append(f(x2[count]))
        print("Valor de fx2: ",fx2[count])
        h0.append(x1[count]-x0[count])
        print("Valor de h0: ",h0[count])
        h1.append(x2[count]-x1[count])
        print("Valor de h1: ",h1[count])

        if(h1 == 0 or h0 == 0):
            itr = count + 1
            break

        d0.append((fx1[count]-fx0[count])/h0[count])
        print("Valor de d0: ",d0[count])
        d1.append((fx2[count]-fx1[count])/h1[count])
        print("Valor de d1: ",d1[count])
        a.append((d1[count]-d0[count])/(h1[count]+h0[count]))
        print("Valor de a: ",a[count])
        b.append((a[count]*h1[count])+d1[count])
        print("Valor de b: ",b[count])
        c.append(fx2[count])
        print("Valor de c: ",c[count])
        print("\n")

        discriminante = pow(b[count],2)-(4*a[count]*c[count])

        if discriminante > 0:

            if(b[count] > 0):
                denominador = b[count]+(sqrt(discriminante))
            else:
                denominador = b[count]-(sqrt(discriminante))

            if denominador != 0:
                x3.append(x2[count]-((2*c[count])/(denominador)))
            else:
                itr = count + 1
                break
        else:
            itr = count + 1
            break

        fx3.append(f(x3[count]))

        x0.append(x1[count])
        x1.append(x2[count])
        x2.append(x3[count])

        if(count > 0):
            error = abs((x2[count]-x2[count-1])/x2[count])
            err.append(error)
            if(error < float(errorEstimado) or error == 0):
                itr = count + 1
                count = 100 #or break
        else:
            err.append(100)

        count=count+1
    
    context = {
        "metodo":"muller",
        "count":range(itr),
        "nCate":range(4),
        "cate":["x0","x1","x2","Error"],
        "x0":x0,
        "x1":x1,
        "x2":x2,
        "err":err,
    }
    
    print("Valores de x2: ",x2)
    print("Errores: ",err)
    print("\n")

    return context

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
            context = metodo_puntoFijo(funcionF, funcionG, puntoA, error, truncate)
        if metodo == "muller":
            context = metodo_muller(funcionF, puntoA, puntoB, error, truncate)
        
    return render(request, 'home_view.html', context=context)

