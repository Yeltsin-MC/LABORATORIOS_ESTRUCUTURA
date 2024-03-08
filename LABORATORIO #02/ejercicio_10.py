"""multiplicacion de  dos matrices de diferentes tamaños"""

import numpy as np

# Definir dos matrices con dimensiones compatibles para multiplicación
matriz1 = np.array([[8, 2, 18],
                    [6, 5, 1],
                    [64, 8, 9],
                    [10, 11, 12]])

matriz2 = np.array([[83, 4, 45, 16],
                    [1, 18, 9, 20],
                    [51, 22, 3, 24]])


resultado_multiplicacion = np.dot(matriz1, matriz2) #multipliando raises 


print("Matriz 1:") #mostramos la matriz 1
print(matriz1)

print("\nMatriz 2:") #mostramos la matriz 2
print(matriz2)

print("\nResultado de la multiplicación:")  #
print(resultado_multiplicacion)    #mostramos el resultado de la multiplicación
