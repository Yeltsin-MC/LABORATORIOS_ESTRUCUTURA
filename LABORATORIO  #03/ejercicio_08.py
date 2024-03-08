"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
palíndromos."""

def palindromo(conjunto):
    conjunto2=set()
    for palabra in conjunto:
        reversa = palabra[::-1]
        if palabra == reversa:
            conjunto2.add(palabra)
    return conjunto2

palabras ={'juan','ana','maria','solos','kati'}         #el punto .lower hace que si ponesmos un valor en mayuscula lo comvierte a minuscula
c = palindromo(palabras)
print(c)