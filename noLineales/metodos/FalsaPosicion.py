from sympy import *

#Método de Falsa Posición

def metodo_posicion_falsa(express, puntoA, puntoB, errorEstimado, truncate):
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
        "funcionF":express,
        "puntoA":puntoA,
        "puntoB":puntoB,
        "error":errorEstimado,
        "truncate":truncate,
    }
    print(context)

    return context