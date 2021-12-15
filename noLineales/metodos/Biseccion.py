from sympy import *

#Método de Bisección

def metodo_biseccion(express, puntoA, puntoB, errorEstimado, truncate):
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
        "funcionF":express,
        "puntoA":puntoA,
        "puntoB":puntoB,
        "error":errorEstimado,
        "truncate":truncate,
    }

    return context