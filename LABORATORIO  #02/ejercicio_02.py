""" Escribe una función recursiva que imprima la suma de los números del 1 al n. """

def suma_numeros_hasta_n(n): #Función recursiva que imprime la suma de los números del 1 al n
    if n == 1:
        return 1  # caso base la suma de los números hasta 1 es 1
    else:
        suma = n + suma_numeros_hasta_n(n - 1)  # llamada recursiva con el número anterior
        print(f"Suma hasta {n}: {suma}")  # imprime la suma hasta el número actual
        return suma

# llamada inicial a la función con el valor deseado de n
resultado = suma_numeros_hasta_n(10)  # Puedes cambiar 10 por el valor deseado
print(f"Resultado final: {resultado}")
