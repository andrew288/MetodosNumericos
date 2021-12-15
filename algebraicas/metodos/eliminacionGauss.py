# Eliminación Gaussiana
import numpy as np

def eliminacionGauss(matriz):
    matrices = []
    # Orden de la matriz
    orden = len(matriz)
    # Recorrer la matriz
    for j in range(0, orden + 1):
        for i in range(0, orden):
            if i > j:
                # Divir los elementos de la matriz
                division = matriz[i][j] / matriz[j][j]
                for k in range(0, orden + 1):
                    # Obterner el nuevo valor para los elementos en la diagonal inferior
                    matriz[i][k] = matriz[i][k] - division * matriz[j][k]
                matrices.append(matriz)

    # Recorrer la matriz
    x = np.zeros(orden)
    for i in range(orden, 0, -1):
        suma = 0
        for j in range(i, orden):
            suma = suma + matriz[i - 1][j] * x[j]
            # Obtener los valores de las variables
        x[i - 1] = ((matriz[i - 1][orden] - suma) / matriz[i - 1][i - 1])
    # Mostrar los valores de las variables
    # for i in range(0,orden):
    # print("x"+str(i)+" = "+str(x[i]))
    dic = {
        'matrices': matrices,
        'respuesta': list(x)
    }
    return dic