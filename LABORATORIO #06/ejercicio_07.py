"""Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo). 
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(raiz):
    """
    Función que cuenta la cantidad de nodos internos en un árbol.

    :param raiz: Nodo raíz del árbol.
    :return: Cantidad de nodos internos.
    """
    # Si el nodo tiene al menos un hijo, es un nodo interno
    if raiz.hijos:
        nodos_internos = 1  # Contamos el nodo actual como interno
    else:
        nodos_internos = 0  # El nodo actual es una hoja
    
    # Recorremos los hijos del nodo actual
    for hijo in raiz.hijos:
        # Sumamos la cantidad de nodos internos en el subárbol
        nodos_internos += contar_nodos_internos(hijo)
    
    return nodos_internos

# Ejemplo de uso:
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos = [Nodo(2), Nodo(3), Nodo(4)]
raiz.hijos[0].hijos = [Nodo(5), Nodo(6)]
raiz.hijos[1].hijos = [Nodo(7)]
raiz.hijos[2].hijos = []

# Contar nodos internos
cantidad_nodos_internos = contar_nodos_internos(raiz)
print(f'La cantidad de nodos internos en el árbol es: {cantidad_nodos_internos}')
