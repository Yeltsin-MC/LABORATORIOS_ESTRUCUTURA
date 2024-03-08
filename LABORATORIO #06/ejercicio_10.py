"""10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol. 
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_minimo_en_arbol(raiz):
    """
    Función que encuentra el nodo con el valor mínimo en un árbol.

    :param raiz: Nodo raíz del árbol.
    :return: Nodo con el valor mínimo.
    """
    # Si el árbol está vacío (raíz es None), devolvemos None
    if raiz is None:
        return None
    
    # Inicializamos el nodo mínimo con la raíz
    nodo_minimo = raiz
    
    # Recorremos los hijos del nodo actual
    for hijo in raiz.hijos:
        # Llamada recursiva para encontrar el mínimo en cada subárbol
        nodo_minimo_hijo = encontrar_minimo_en_arbol(hijo)
        
        # Actualizamos el nodo mínimo si encontramos uno con un valor menor
        if nodo_minimo_hijo.valor < nodo_minimo.valor:
            nodo_minimo = nodo_minimo_hijo
    
    return nodo_minimo

# Ejemplo de uso:
# Crear un árbol de ejemplo
raiz = Nodo(10)
raiz.hijos = [Nodo(5), Nodo(8), Nodo(12)]
raiz.hijos[0].hijos = [Nodo(3), Nodo(7)]
raiz.hijos[1].hijos = [Nodo(6)]
raiz.hijos[2].hijos = [Nodo(15), Nodo(2)]

# Encontrar el nodo con el valor mínimo en el árbol
nodo_minimo = encontrar_minimo_en_arbol(raiz)
print(f'El nodo con el valor mínimo es: {nodo_minimo.valor}')
