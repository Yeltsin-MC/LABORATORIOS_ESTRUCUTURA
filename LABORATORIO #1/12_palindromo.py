
def es_palindromo(palabra):# Función para verificar si una palabra es un palíndromo


    palabra = palabra.lower().replace(" ", "") # Convertimos la palabra a minúsculas y eliminamos los espacios

    return palabra == palabra[::-1]    # Comparar la palabra con su inversa


# Obtener la entrada del usuario
palabra = input("Ingresa una palabra para verificar si es un palíndromo: ")

if es_palindromo(palabra):# Verificamos si es un palíndromo o no

    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
