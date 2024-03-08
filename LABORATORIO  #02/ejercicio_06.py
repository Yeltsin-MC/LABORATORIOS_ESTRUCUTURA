"""Crea una matriz de números reales."""

def crear_matriz(filas, columnas):
    matriz = []  # inicializa la matriz vacía

    for i in range(filas):
        fila = []  # inicializa cada fila como una lista vacía
        for j in range(columnas):
            # puedes modificar esta línea para ingresar los valores deseados
            valor = float(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
            fila.append(valor)  # Agrega el valor a la fila
        matriz.append(fila)  # Agrega la fila a la matriz

    return matriz

# matriz 3x3
filas = 3
columnas = 3
matriz_numeros_reales = crear_matriz(filas, columnas)

# Imprime la matriz
for fila in matriz_numeros_reales:
    print(fila)
