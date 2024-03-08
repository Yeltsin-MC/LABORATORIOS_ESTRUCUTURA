#Escriba una función que reciba dos conjuntos de números 
#y devuelva un conjunto con los números que están en el primer conjunto pero no en el segundo.



def diferencia_entre_conjuntos(primer_conjunto , segundo_conjunto):     #devuelven los elementos del primer conjunto pero no en el segundo
    diferencia = primer_conjunto - segundo_conjunto
    return diferencia


conjunto1 = {1, 2, 3, 4, 5}          #ejemplo
conjunto2 = {3, 4, 5, 6, 7}

resultado = diferencia_entre_conjuntos(conjunto1 ,conjunto2)

print(resultado)
