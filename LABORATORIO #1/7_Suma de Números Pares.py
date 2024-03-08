"Calcula la suma de los números pares en un rango especificado por el usuario"

inicio = int(input("Ingresa el número de comienzo: "))
fin = int(input("Ingresa el número final del rango: "))


suma_pares=0
for numero in range(inicio, fin + 1):   #calcula la suma de los numeros según al rango
    suma_pares
    if numero % 2 == 0:
        suma_pares += numero


print(f"La suma de los números pares en el rango  es: {suma_pares}")
