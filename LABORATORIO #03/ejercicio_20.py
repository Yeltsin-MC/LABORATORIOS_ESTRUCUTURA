"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor."""

def palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud):  

    #filtramos palabras palíndromas y con la longitud deseada
    palindromas_longitud = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1] and len(palabra) == longitud}  
    
    #  el conjunto resultante y convertirlo de nuevo a un conjunto
    conjunto_palindromas_longitud_ordenadas = set(sorted(palindromas_longitud))
    
    # devueleve el conjunto ordenado de palíndromas con la longitud deseada
    return conjunto_palindromas_longitud_ordenadas


conjunto_palabras = {'radar', 'oso', 'casa', 'nivel', 'reconocer', 'python'}
longitud_deseada = 3
conjunto_resultante = palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud_deseada)
print(conjunto_resultante)


