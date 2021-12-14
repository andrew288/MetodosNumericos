from sympy import *
from math import sqrt
from math import pow

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