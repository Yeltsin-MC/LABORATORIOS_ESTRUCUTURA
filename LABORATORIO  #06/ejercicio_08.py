"""implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
hasta una hoja). """

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_altura(raiz):
    """
    Función que calcula la altura de un árbol.

    :param raiz: Nodo raíz del árbol.
    :return: Altura del árbol.
    """
    # Si el árbol está vacío (raíz es None), la altura es 0
    if raiz is None:
        return 0
    
    # Si el árbol tiene hijos, calculamos la altura recursivamente
    if raiz.hijos:
        # Calculamos la altura de cada subárbol y tomamos el máximo
        alturas_hijos = [calcular_altura(hijo) for hijo in raiz.hijos]
        return 1 + max(alturas_hijos)
    else:
        # Si el nodo actual es una hoja, la altura es 1
        return 1

# Ejemplo de uso:
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos = [Nodo(2), Nodo(3), Nodo(4)]
raiz.hijos[0].hijos = [Nodo(5), Nodo(6)]
raiz.hijos[1].hijos = [Nodo(7)]
raiz.hijos[2].hijos = []

# Calcular altura del árbol
altura_arbol = calcular_altura(raiz)
print(f'La altura del árbol es: {altura_arbol}')
