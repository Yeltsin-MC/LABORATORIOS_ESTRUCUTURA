"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
palíndromos y están ordenadas de menor a mayor.
"""
def palabras_palindromas_ordenadas(conjunto_palabras):         
    palindromas = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    return set(sorted(palindromas))


conjunto_palabras = {'radar', 'oso', 'casa', 'nivel', 'reconocer', 'python'}
conjunto_palindromas_ordenadas = palabras_palindromas_ordenadas(conjunto_palabras)
print(conjunto_palindromas_ordenadas)