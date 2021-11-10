from django.shortcuts import render 
from sympy import *
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
            if(error < 0.0001 or error == 0):
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
        
    return render(request, 'home_view.html', context=context)

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

def index(request):
    context={}
    return render(request,'index.html',context={})

def metodo_newton_raphson(express,puntoA):
    print("Metodo Newton Raphson")
    #declaracion de variables
    x = symbols('x')
    #variables necesarias
    str_expr = ""
    count = 0
    itr = 0
    
    xn = []
    xr = []
    fxn = []
    dfxn = []

    err = []
    error = 0
    #parse funcion ingresada
    str_expr = express
    expr= sympify(str_expr, evaluate=False)
    f = lambdify(x,expr)
    df = lambdify(x,diff(expr,x))
    #asignacion de puntos iniciales
    xn.append(float(puntoA))


    #iteraciones
    while(count<100):
        fxn.append(f(xn[count]))
        dfxn.append(df(xn[count]))


        xr.append(xn[count]-((fxn[count])/(dfxn[count])))

        xn.append(xr[count])

        
        if(count>0):
            error = abs((xr[count]-xr[count-1])/xr[count])
            err.append(error)
            if(error == 0):
                itr = count + 1
                count = 100
        else:
            err.append(100)

        count=count+1

    #pasamos nuestros valores
    context = {
        "metodo":"newtonRaphson",
        "count":range(itr),
        "xn":xn,
        "xr":xr,
        "fxn":fxn,
        "dfxn":dfxn,
        "err":err,
    }

    return context
    

def metodo_secante(express,puntoA):
    print("Metodo Secante")
    #declaracion de variables
    x = symbols('x')
    str_expr = ""
    count = 0
    itr = 0

    xi = []
    xi_1 = []
    fxi = []
    fxi_1 = []
    xr = []

    err = []
    error = 0

    #parse funcion ingresada
    str_expr = express
    expr= sympify(str_expr, evaluate=False)
    f = lambdify(x,expr)
    #asignacion de puntos iniciales

    puntoStr = str(float(puntoA))
    puntoStr = puntoStr[puntoStr.find(".")+1:]

    print((10**(len(puntoStr)))**-1)

    minDif = ((10**(len(puntoStr)))**-1)
    xi.append(float(puntoA))
    xi_1.append(float(puntoA)+float(minDif))

    print(xi[0], "  " , xi_1[0])
    
    while(count<100):
        fxi.append(f(xi[count]))
        fxi_1.append(f(xi_1[count]))


        xr.append(xi[count]-(fxi[count]*(xi_1[count]-xi[count]))/(fxi_1[count]-fxi[count]))

        xi.append(xr[count])

        xi_1.append(xi[count])
        
        if(count>0):
            error = abs((xr[count]-xr[count-1])/xr[count])
            err.append(error)
            if(error == 0):
                itr = count + 1
                count = 100
        else:
            err.append(100)

        count=count+1


    context = {
        "metodo":"secante",
        "count":range(itr),
        "xi":xi,
        "xi_1":xi_1,
        "fxi":fxi,
        "fxi_1":fxi_1,
        "xr":xr,
        "err":err,
    }
    
    return context


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
            context =  metodo_newton_raphson(funcion, puntoA)
        if metodo == "secante":
            context = metodo_secante(funcion, puntoA)

        
    return render(request, 'mabiertos.html', context=context)
