
from sympy import *
#Método de Newton Raphson

def metodo_nr_modificado(express,puntoA, errorEstimado):
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
    ddfxn = []
    dfxn2 = []

    err = []
    error = 0
    #parse funcion ingresada
    str_expr = express
    expr= sympify(str_expr, evaluate=False)
    f = lambdify(x,expr)
    df = lambdify(x,diff(expr,x))
    ddf =lambdify(x,diff(expr,x,2))
    #asignacion de puntos iniciales
    xn.append(float(puntoA))


    #iteraciones
    while(count<100):
        fxn.append(f(xn[count]))
        dfxn.append(df(xn[count]))
        ddfxn.append(ddf(xn[count]))
        dfxn2.append(dfxn[count]*dfxn[count])
        xr.append(xn[count]-((fxn[count])*(dfxn[count])/(dfxn2[count]-(fxn[count])*(ddfxn[count]))))
        xn.append(xr[count])   
        if(count>0):
            error = abs((xr[count]-xr[count-1])/xr[count])
            err.append(error)
            if(error <= float(errorEstimado)):
                itr = count + 1
                count = 100
        else:
            err.append(100)

        count=count+1

    #pasamos nuestros valores
    context = {
        "metodo":"newtonRaphsonModificado",
        "count":range(itr),
        "xn":xn,
        "xr":xr,
        "fxn":fxn,
        "dfxn":dfxn,
        "dfxn2":dfxn2,
        "ddfxn":ddfxn,
        "err":err,
    }

    return context