""" Escribe una función recursiva que imprima los números pares del 1 al 100. """

def imprimir_pares(numero): #imprime los números pares del 1 al 100
    if numero <= 100:
        if numero % 2 == 0:
            print(numero, end=" ")  # imprime el número par actual
        imprimir_pares(numero + 1)  # llamada recursiva con el siguiente número

# llamada inicial a la función con el primer número
imprimir_pares(1)
