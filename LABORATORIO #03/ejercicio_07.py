
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas.

def anagramas_palabras(palabra1, palabra2):
    return palabra1 == palabra2     #verificamos si la palabraa es anagrama
                                                      # sorted ordena elemento de la secuencia
def anagramas_conjunto(conjunto_palabras):
    anagramas = set()

    for palabra1 in conjunto_palabras:
        for palabra2 in conjunto_palabras:
            if palabra1 != palabra2 and anagramas_palabras(palabra1, palabra2):         #comparamos si son diferentes y anagramas
                anagramas.add(palabra1)
                anagramas.add(palabra2)

    return anagramas

# Ejemplo de uso
palabras = {"roma", "loma", "amor", "oso", "hola", "rio"}
resultado = anagramas_conjunto(palabras)
print(resultado)
