"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no
están duplicados"""


def diferencia(a,b):            #funcion de elementos que se repite
    conjunto_diferencia1=(b.difference(a))   #crea el conjunto intersección
    conjunto_diferencia2=(a.difference(b))   #crea el conjunto intersección

    return conjunto_diferencia1 and conjunto_diferencia2


A={4,8,6,2,10,12,17,5}
B={1,8,5,6,12,14,11,22}

c=diferencia(A,B)  #pasamos los conjuntos
print(c)