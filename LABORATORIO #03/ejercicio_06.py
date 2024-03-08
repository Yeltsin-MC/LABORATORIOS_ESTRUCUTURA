"""Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
están en el segundo conjunto pero no en el primero.
"""
def diferencia(a,b):            #funcion de elementos que se repite
    conjunto_diferencia=(b.difference(a))   #crea el conjunto intersección
    
    return conjunto_diferencia


A={4,8,6,2,10,12,17,5}
B={1,8,5,6,12,14,11,22}

c=diferencia(A,B)  #pasamos los conjuntos
print(c)
