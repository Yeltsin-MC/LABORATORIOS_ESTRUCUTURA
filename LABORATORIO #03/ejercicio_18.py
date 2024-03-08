""" Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
contienen una letra determinada y están ordenadas de mayor a menor"""

def palabras_con_letra(conjunto_palabras, letra):

    # Utilizar un conjunto por comprensión para filtrar palabras que contienen la letra deseada
    conjunto_palabras_con_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    return conjunto_palabras_con_letra

conjunto_palabras = {"osculo", "dieron", "pasada", "romper", "torcer"}

letra_deseada = str(input("Ingresar palabra deseada: ")).lower()   #aqui pedimos la letra deceada


palabras_con_letra = palabras_con_letra(conjunto_palabras, letra_deseada)  # Llamar a la función y almacenar el conjunto resultante en una variable

print(f"Conjunto de palabras con la letra '{letra_deseada}':", palabras_con_letra)