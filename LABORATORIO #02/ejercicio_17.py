"""Escribe una función que encuentre la matriz de covarianza de dos matrices."""

def media(lista):                   #saca la media
    return sum(lista) / len(lista)

def covarianza(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        raise ValueError("Las matrices deben tener el mismo número de filas")

    n = len(matriz1)  # número de filas
    m = len(matriz1[0])  # número de columnas

    # Calcular medias de cada columna en ambas matrices
    media_matriz1 = [media(matriz1[i]) for i in range(n)]
    media_matriz2 = [media(matriz2[i]) for i in range(n)]

    # Inicializar la matriz de covarianza
    cov_matrix = [[0] * m for _ in range(m)]

    # Calcular la covarianza para cada par de columnas
    for i in range(m):
        for j in range(m):
            
            # Fórmula de covarianza
            
            cov_ij = sum((matriz1[k][i] - media_matriz1[i]) * (matriz2[k][j] - media_matriz2[j]) for k in range(n)) / (n - 1)   
            cov_matrix[i][j] = cov_ij

    return cov_matrix

# Ejemplo de uso
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matriz_cov = covarianza(matriz1, matriz2)

print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nMatriz de covarianza:")     #imprime los resultados
for fila in matriz_cov:
    print(fila)