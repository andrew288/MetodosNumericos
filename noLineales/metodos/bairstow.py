from sympy import *

def round_list(list_real):
    i = 0
    count = len(list_real)
    while i < count:
        aux = list_real[i]
        aux = aux.round(4)
        list_real[i] = aux
        i += 1
    return list_real


def reverse_list(list_real):
    list_aux = []
    for i in reversed(list_real):
        list_aux.append(i)
    round_list(list_aux)
    return list_aux


def get_a(expr, x):
    polinomy = Poly(expr, x)
    a = polinomy.coeffs()
    a.reverse()
    return round_list(a)


def get_b(coeff_a, r, s):
    aux_b = []
    aux_b.append(coeff_a[-1])
    aux_b.append(coeff_a[-2] + (r * aux_b[0]))
    for i in range(3, len(coeff_a) + 1):
        aux = coeff_a[(-1 * i)] + (r * aux_b[-1]) + (s * aux_b[-2])
        aux_b.append(aux)
    aux_b.reverse()
    return round_list(aux_b)


def get_c(coeff_b, r, s):
    aux_c = []
    aux_c.append(coeff_b[-1])
    aux_c.append(coeff_b[-2] + (r * aux_c[0]))

    for i in range(3, len(coeff_b)):
        aux = coeff_b[(-1 * i)] + (r * aux_c[-1]) + (s * aux_c[-2])
        aux_c.append(aux)
    aux_c.reverse()
    return round_list(aux_c)

def array_head(array_b, array_c):
    array_header = ["r", "s", "R", "S", "Ear", "Eas"]
    return array_header
def bairstow(expr, error, r, s):
    x = Symbol('x')
    expression = sympify(expr)
    f = lambdify(x, expression)

    array_b = []
    array_c = []
    array_r = []
    array_s = []

    array_Ar = []
    array_As = []
    array_Ear = []
    array_Eas = []

    #error = 0.01
    e_r = 1
    e_s = 1

    while (e_r >= error and e_s >= error):
        a = get_a(expression, x)
        b = get_b(a, r, s)
        c = get_c(b, r, s)
        array_b.append(b)
        array_c.append(c)

        A_r = (c[2] * b[0] - c[1] * b[1]) / (c[1] * c[1] - c[0] * c[2])
        A_s = (c[0] * b[1] - c[1] * b[0]) / (c[1] * c[1] - c[0] * c[2])
        array_Ar.append(A_r)
        array_As.append(A_s)

        r = r + A_r
        s = s + A_s
        array_r.append(r)
        array_s.append(s)

        e_r = abs(A_r / r)
        e_s = abs(A_s / s)
        array_Ear.append(e_r)
        array_Eas.append(e_s)

    x1 = (r + pow(pow(r, 2) + 4 * s, 0.5)) / 2
    x2 = (r - pow(pow(r, 2) + 4 * s, 0.5)) / 2

    if (isinstance(x1, complex)):
        x1.real = round(x1.real, 4)
        x1.imag = round(x1.imag, 4)
    else:
        x1 = round(x1, 4)
    if (isinstance(x2, complex)):
        x2.real = round(x2.real, 4)
        x2.imag = round(x2.imag, 4)
    else:
        x2 = round(x2, 4)

    dic = {
        'head': array_head(array_b, array_c),
        'count': range(len(array_r)),
        'b': array_b,
        'c': array_c,
        'r': array_r,
        's': array_s,
        'Ar': array_Ar,
        'As': array_As,
        'Er': array_Ear,
        'Es': array_Eas,
        'x1': x1,
        'x2': x2
    }
    return dic
