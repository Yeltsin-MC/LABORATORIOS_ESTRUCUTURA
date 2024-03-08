""" Escribe una función recursiva que imprima la tabla de multiplicar del n. """

def imprimir_tabla_multiplicar(n, multiplicador=1):
    if multiplicador > 10:
        return  # se han impreso todas las filas (hasta 10)

    resultado = n * multiplicador
    print(f"{n} x {multiplicador} = {resultado}")

    # llamada recursiva con el siguiente multiplicador
    imprimir_tabla_multiplicar(n, multiplicador + 1)

# lamada inicial a la función con el valor deseado de n
imprimir_tabla_multiplicar(5)  # Puedes cambiar 5 por el valor deseado
