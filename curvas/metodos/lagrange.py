# Interpolacion de Lagrange
# DivisoresL solo para mostrar valores
import numpy as np
import sympy as sym


def lagrange(xi, fi):
    # Polinomio de Lagrange
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype=float)
    for i in range(0, n, 1):
        numerador = 1
        denominador = 1
        for j in range(0, n, 1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    #simplifica el polinomio
    polisimple = polinomio.expand().evalf(5)

    dic = {
        'respuesta': str(polisimple),
        'divisoresL': list(divisorL)
            }
    return dic
