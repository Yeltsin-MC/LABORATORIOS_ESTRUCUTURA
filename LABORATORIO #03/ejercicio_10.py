"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
contienen una letra determinada.
"""


def palabras_con_letra(conjunto_palabras, letra): #busca las palabras con una letra especifica
    
    conjunto_palabras_con_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    return conjunto_palabras_con_letra

conjunto_palabras = {"osculo", "dieron", "pasada", "romper", "torcer"}
letra_deseada = str(input("Ingresar palabra deseada: ")).lower()
palabras_con_letra = palabras_con_letra(conjunto_palabras, letra_deseada)
print(f"Conjunto de palabras con la letra '{letra_deseada}':", palabras_con_letra)