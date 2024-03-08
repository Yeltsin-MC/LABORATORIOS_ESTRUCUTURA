"""Escribe una función que encuentre la submatriz de mayor suma de una matriz.
"""
def submatriz_maxima(matriz):  #creamos una función para saber si esta correcto o no 
    if not matriz or not matriz[0]:
        raise ValueError("La matriz está vacía o tiene dimensiones incorrectas")

    filas, columnas = len(matriz), len(matriz[0])  #cuenta los eleementos

    maxima_suma = float('-inf')      # Inicializar con un valor negativo infinito
    resultado = None

    for i in range(filas):
                                 # Inicializar un array para almacenar las sumas acumulativas de la columna actual
        suma_acumulativa = [0] * columnas

        for j in range(i, filas):
                                                                                # Actualizar la suma acumulativa con la nueva fila
            for k in range(columnas):
                suma_acumulativa[k] += matriz[j][k]

                                                                # Aplicar el algoritmo de Kadane para encontrar la sublista de suma máxima
            maxima_suma_local = float('-inf')
            inicio_local = 0
            for k in range(columnas):
                if suma_acumulativa[k] > maxima_suma_local + suma_acumulativa[k]:
                    maxima_suma_local = suma_acumulativa[k]
                    inicio_local = k
                else:
                    maxima_suma_local += suma_acumulativa[k]

                                                                    # Actualizar el resultado si encontramos una suma mayor
                if maxima_suma_local > maxima_suma:
                    maxima_suma = maxima_suma_local
                    resultado = [(i, inicio_local), (j, k)]

    return resultado

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

submatriz_maxima_resultado = submatriz_maxima(matriz_ejemplo)

                                                    # Mostrar la matriz y la submatriz de mayor suma
print("Matriz:")        # Mostrar la matriz y la submatriz de mayor suma

for fila in matriz_ejemplo:
    print(fila)

print("\nSubmatriz de mayor suma:")  # Verificar si hay una submatriz de mayor suma

if submatriz_maxima_resultado:
    inicio, fin = submatriz_maxima_resultado
    for i in range(inicio[0], fin[0] + 1):      # Mostrar la submatriz

        print(matriz_ejemplo[i][inicio[1]:fin[1] + 1])
else:
    print("No hay submatriz de mayor suma.")
