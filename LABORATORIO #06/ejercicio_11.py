"""11. Implementar una función que encuentre el nodo con el valor máximo en el árbol. 
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_maximo_en_arbol(raiz):
    """
    Encuentra el nodo con el valor máximo en un árbol.

    :param raiz: Nodo raíz del árbol.
    :return: Nodo con el valor máximo.
    """
    # Si el árbol está vacío (raíz es None), devolvemos None
    if raiz is None:
        return None
    
    # Inicializamos el nodo máximo con la raíz
    nodo_maximo = raiz
    
    # Recorremos los hijos del nodo actual
    for hijo in raiz.hijos:
        # Llamada recursiva para encontrar el máximo en cada subárbol
        nodo_maximo_hijo = encontrar_maximo_en_arbol(hijo)
        
        # Actualizamos el nodo máximo si encontramos uno con un valor mayor
        if nodo_maximo_hijo.valor > nodo_maximo.valor:
            nodo_maximo = nodo_maximo_hijo
    
    return nodo_maximo

# Ejemplo de uso:
# Crear un árbol de ejemplo
raiz = Nodo(10)
raiz.hijos = [Nodo(5), Nodo(8), Nodo(12)]
raiz.hijos[0].hijos = [Nodo(3), Nodo(7)]
raiz.hijos[1].hijos = [Nodo(6)]
raiz.hijos[2].hijos = [Nodo(15), Nodo(2)]

# Encontrar el nodo con el valor máximo en el árbol
nodo_maximo = encontrar_maximo_en_arbol(raiz)
print(f'El nodo con el valor máximo es: {nodo_maximo.valor}')
