from sympy import *

#Método de Graeffe

def metodo_graeffe(a0, a1, a2, a3):
    iteracion = 0
    it = []
    aa0 = []
    aa1 = []
    aa2 = []
    aa3 = []

    a0 = float(a0)
    a1 = float(a1)
    a2 = float(a2)
    a3 = float(a3)
    if(a0 != 1):
        print("a0 es diferente de 1")
        print("a0 "+str(a0))
        aux = a0
        a0 = a0/aux
        a1 = a1/aux
        a2 = a2/aux
        a3 = a3/aux
    seguir = 0

    while(seguir < 16):
        it.append(iteracion)
        aa0.append(a0)
        aa1.append(a1)
        aa2.append(a2)
        aa3.append(a3)

        #imprimir
        print('iteracion: '+str(iteracion))
        print(a0)
        print(a1)
        print(a2)
        print(a3)
        #variables de repuesto
        a1m = a1
        a2m = a2
        a3m = a3
        #nueva iteracion
        try:
            a1 = 2*a2m - a1m**2
            a2 = a2m**2 - 2*a1m*a3m
            a3 = -a3m**2
        except:
            print("TERMINA")
            break
        if(a1 == a1m and a2 == a2m and a3 == a3m):
            print("Se repiten valores iguales")
            break
        a1abs = abs(a1)
        a2abs = abs(a2)
        a3abs = abs(a3)
        m2 = 2**iteracion
        r1 = a1abs**(1/m2)
        r2 = (a2abs/a1abs)**(1/m2)
        r3 = (a3abs/a2abs)**(1/m2)
        print('raiz en la it '+str(iteracion)+" : "+str(r1))
        print('raiz en la it '+str(iteracion)+" : "+str(r2))
        print('raiz en la it '+str(iteracion)+" : "+str(r3))
        iteracion+=1
        seguir+=1
    #Raices
    a1abs = abs(a1)
    a2abs = abs(a2)
    a3abs = abs(a3)
    m2 = 2**iteracion
    print("iteracion final ES: "+str(iteracion))
    print(a1abs)
    print(a2abs)
    print(a3abs)
    print('2 a la m es '+str(m2))

    r1 = a1abs**(1/m2)
    r2 = (a2abs/a1abs)**(1/m2)
    r3 = (a3abs/a2abs)**(1/m2)
    print('raiz en la it: '+str(iteracion)+str(r1))
    print('raiz en la it: '+str(iteracion)+str(r2))
    print('raiz en la it: '+str(iteracion)+str(r3))
    context = {
        "metodo":"graeffe",
        "count":range(iteracion),
        "it":it,
        "a0":aa0,
        "a1":aa1,
        "a2":aa2,
        "a3":aa3,
        "r1":r1,
        "r2":r2,
        "r3":r3,
    }

    return context

