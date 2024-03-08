"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
están ordenados de mayor a menor."""

def ordenador_conjunto(conjunto):
    conjunto_ordenado = sorted(list(conjunto), reverse=True)  #sorted hace que se ordene y el reverse=true hace que sea de mayor a menor

    return conjunto_ordenado              

# Ejemplo de uso
conjunto1 = {8, 1, 6, 2, 10, 12, 17, 5}
conjunto_ordenado = ordenador_conjunto(conjunto1)
print(conjunto_ordenado)