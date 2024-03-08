"""6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos). 
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(raiz):
    """
    Función que cuenta la cantidad de nodos hoja en un árbol.

    :param raiz: Nodo raíz del árbol.
    :return: Cantidad de nodos hoja.
    """
    # Si el nodo no tiene hijos, es un nodo hoja
    if not raiz.hijos:
        return 1
    
    # Inicializamos el contador de nodos hoja
    nodos_hoja = 0
    
    # Recorremos los hijos del nodo actual
    for hijo in raiz.hijos:
        # Sumamos la cantidad de nodos hoja en el subárbol
        nodos_hoja += contar_nodos_hoja(hijo)
    
    return nodos_hoja

# Ejemplo de uso:
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos = [Nodo(2), Nodo(3), Nodo(4)]
raiz.hijos[0].hijos = [Nodo(5), Nodo(6)]
raiz.hijos[1].hijos = [Nodo(7)]
raiz.hijos[2].hijos = []

# Contar nodos hoja
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print(f'La cantidad de nodos hoja en el árbol es: {cantidad_nodos_hoja}')
