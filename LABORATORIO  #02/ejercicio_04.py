""" Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n."""

def imprimir_piramide_invertida(n, current_row=1):
    
    if current_row > n:
        return  #todas las filas han sido impresas
    else:
        # se imprime espacios en blanco para alinear los números correctamente
        for i in range(n - current_row):
            print(" ", end=" ")

        # se imprime los números en orden descendente
        for i in range(current_row, 0, -1):
            print(i, end=" ")
        print()  # salto de línea después de imprimir la fila

        # llamada recursiva con la siguiente fila
        imprimir_piramide_invertida(n, current_row + 1)

# Llamada inicial a la función con el valor deseado de n
imprimir_piramide_invertida(5)  # Puedes cambiar 5 por el valor deseado
