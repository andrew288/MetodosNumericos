from sympy import *

#Método de Newton Raphson

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
    