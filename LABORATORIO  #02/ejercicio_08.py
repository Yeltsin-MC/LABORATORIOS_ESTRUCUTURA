"""Crea una matriz de matrices. """

def crear_matriz_de_matrices(filas, columnas, tamano_submatriz):
    matriz = []  # inicializa la matriz principal vacía

    for i in range(filas):
        fila = []  # inicializa cada fila como una lista vacía
        for j in range(columnas):
            # crea una submatriz con las dimensiones especificadas
            submatriz = [[0] * tamano_submatriz[1] for _ in range(tamano_submatriz[0])]
            fila.append(submatriz)  # Agrega la submatriz a la fila
        matriz.append(fila)  # agrega la fila a la matriz principal

    return matriz

# matriz 2x2 de matrices 3x3
filas = 2
columnas = 2
tamano_submatriz = (3, 3)
matriz_de_matrices = crear_matriz_de_matrices(filas, columnas, tamano_submatriz)

# Imprime la matriz de matrices
for fila in matriz_de_matrices:
    for submatriz in fila:
        print(submatriz)
    print()
