"""Escribe una función que encuentre el elemento máximo de una matriz."""

def encontrar_maximo(matriz):
                                        # verificamos si la matriz tiene dimensiones incorrectas
    if not matriz or not matriz[0]:
        raise ValueError("La matriz está vacía o tiene dimensiones incorrectas")

    maximo = matriz[0][0]  # inicializamos con el primer elemento

    for fila in matriz:            # Iteramos  las filas y columnas de la matriz
        for elemento in fila:
            if elemento > maximo:               # Comparar cada elemento con el máximo actual
                maximo = elemento

    return maximo

matriz_ejemplo = [             #matriz ejemplo
    [1, 5, 3],
    [9, 2, 8],
    [4, 7, 6]
]

maximo = encontrar_maximo(matriz_ejemplo)

print("Matriz:")
for fila in matriz_ejemplo:    #imprimimos la matriz
    print(fila)

print("\nElemento máximo de la matriz:", maximo)   #imprimimos el resultado
