from sympy import *

#Método de Secante

def metodo_secante(express,puntoA,errorEstimado):
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
        if (fxi_1[count]-fxi[count]) == 0 :
            xr.append(float(puntoA))
        else :
            xr.append(xi[count]-(fxi[count]*(xi_1[count]-xi[count]))/(fxi_1[count]-fxi[count]))
        xi.append(xr[count])

        xi_1.append(xi[count])
        
        if(count>0):
            error = abs((xr[count]-xr[count-1])/xr[count])
            err.append(error)
            if(error <= float(errorEstimado)):
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
