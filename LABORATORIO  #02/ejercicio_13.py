"""Crea una matriz de números aleatorios de tamaño 100x100"""

import random                 # importamos el modulo random 
import numpy as np             # importamos modulo matematico 
A=[]
def pedir_filas():                                    # funcion para pedir al usuario el numero de filas
    filas = int(input("Digite el número de filas:"))
    return filas


def pedir_columnas():                                 # funcion para pedir al usuario el numero de columnas
    columnas = int(input("Digite el número de columnas: "))  
    return columnas


def llenar(matriz):                        # función que va crear la matriz
    filas = pedir_filas()
    columnas = pedir_columnas()
    for i in range(filas):                # va iterar las N veces que pusimos agregando un numero random
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(random.randint(1, 100))       #agrega un numero random

llenar(A)            #pasa la lista basia a la función llenar

print("Matriz A con numpy")   #imprimimos
matriz_array = np.array(A)    #creamos una varibales...llamamos a la matriz mediante el modulo np.array (creando una matriz )
print(matriz_array)           # imprimimos la matriz..