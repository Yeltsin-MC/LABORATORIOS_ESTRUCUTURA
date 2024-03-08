""": Escribe una función recursiva que imprima la pirámide de números del 1 al n. """


def imprimir_piramide(n, current_row=1):
    if current_row > n:
        return  # caso base: todas las filas han sido impresas
    else:
        # imprime los numeros de la fila actual
        for i in range(1, current_row + 1):
            print(i, end=" ")
        print()  # salta la línea después de imprimir la fila

        # Llamada recursiva con la siguiente fila
        imprimir_piramide(n, current_row + 1)

# Llamada inicial a la función con el valor deseado de n
imprimir_piramide(5)  # Puedes cambiar 5 por el valor deseado
