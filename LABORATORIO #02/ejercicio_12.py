""" Calcula la media de los elementos de una matriz""" #la suma de sus elementos entre la cantidad de elementos

import numpy as np #importamos el módulo 

                                             # Definir una matriz
matriz = np.array([[5, 10, 6],
                   [4, 5, 4],
                   [2, 8, 6]])

media_matriz = np.mean(matriz)      # Calcular la media de los elementos de la matriz

# Mostrar el resultado
print("Matriz:")
print(matriz)

print("\nMedia de los elementos de la matriz:", media_matriz) #imprime el resultado de la media