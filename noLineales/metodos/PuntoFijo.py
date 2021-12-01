from sympy import *

#Método de Punto Fijo

def metodo_punto_fijo(express, funcionG, puntoA, errorEstimado, truncate):
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