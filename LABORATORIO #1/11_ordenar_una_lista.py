
num = input("Ingresa una lista de números separados por espacios: ")# para dijitar un numero

numeros = [float(numero) for numero in num.split()] # convertimos a una lista de números

numeros_ordenados = sorted(numeros) # "sorted" sirbe para ordenar de menor a mayor


print("Lista ordenada de menor a mayor:", numeros_ordenados)


"""
def ordenar_lista(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


entrada_usuario = input("Ingresa una lista de números separados por espacios: ") #ingresamos la lista de números separados por espacios

lista_numeros = [float(numero) for numero in entrada_usuario.split()] # Convertir la entrada del usuario en una lista de números


ordenar_lista(lista_numeros) # Llamar a la función para ordenar la lista


print("Lista ordenada:", lista_numeros) # imprimimos la lista ordenada

"""
