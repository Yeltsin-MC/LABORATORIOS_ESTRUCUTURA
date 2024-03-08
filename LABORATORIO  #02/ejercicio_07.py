"""Crea una matriz de números complejos. """

def crear_matriz_compleja(filas, columnas):
    matriz = []  # inicializa la matriz vacía

    for i in range(filas):
        fila = []  # inicializa cada fila como una lista vacía
        for j in range(columnas):
            # puedes modificar esta línea para ingresar los valores deseados
            real = float(input(f"Ingrese la parte real para la posición ({i+1}, {j+1}): "))
            imaginaria = float(input(f"Ingrese la parte imaginaria para la posición ({i+1}, {j+1}): "))
            valor_complejo = complex(real, imaginaria)
            fila.append(valor_complejo)  # Agrega el valor a la fila
        matriz.append(fila)  # Agrega la fila a la matriz

    return matriz

# matriz 2x2 de números complejos
filas = 2
columnas = 2
matriz_numeros_complejos = crear_matriz_compleja(filas, columnas)

# Imprime la matriz
for fila in matriz_numeros_complejos:
    print(fila)
