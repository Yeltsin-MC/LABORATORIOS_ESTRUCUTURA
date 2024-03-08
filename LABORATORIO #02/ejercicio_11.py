"""Multiplica una matriz por un número"""

import numpy as np   #importamos el módulo numpy

                                    # ya definimos  una matriz
matriz = np.array([[12, 9, 34],
                   [4, 51, 6],
                   [31, 2, 9]])


n=int(input("Dijiste el multiplicador : ")) 
# Multiplicar la matriz por el escalar
matriz_resultante = n * matriz
                                    # Mostrar el resultado
print("Matriz original:")
print(matriz)

print("\nResultado de la multiplicación por el escalar:") # nueva linea
print(matriz_resultante)                                  #imprimimos la nueva matriz