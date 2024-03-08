"""Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
hasta el nodo). """

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_profundidad(raiz, nodo_busqueda, profundidad_actual=0):
    """
    Función que calcula la profundidad de un nodo en un árbol.

    :param raiz: Nodo raíz del árbol.
    :param nodo_busqueda: Nodo cuya profundidad se quiere calcular.
    :param profundidad_actual: Profundidad actual durante la recursión (por defecto, 0).
    :return: Profundidad del nodo o -1 si el nodo no se encuentra en el árbol.
    """
    # Si la raíz es None, el árbol está vacío
    if raiz is None:
        return -1
    
    # Si encontramos el nodo de búsqueda, devolvemos la profundidad actual
    if raiz.valor == nodo_busqueda:
        return profundidad_actual
    
    # Buscamos en los hijos del nodo actual
    for hijo in raiz.hijos:
        # Llamada recursiva para cada hijo con la profundidad incrementada
        profundidad_hijo = calcular_profundidad(hijo, nodo_busqueda, profundidad_actual + 1)
        
        # Si se encuentra el nodo en alguno de los hijos, devolvemos la profundidad
        if profundidad_hijo != -1:
            return profundidad_hijo
    
    # Si el nodo no se encuentra en el árbol, devolvemos -1
    return -1

# Ejemplo de uso:
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos = [Nodo(2), Nodo(3), Nodo(4)]
raiz.hijos[0].hijos = [Nodo(5), Nodo(6)]
raiz.hijos[1].hijos = [Nodo(7)]
raiz.hijos[2].hijos = []

# Calcular profundidad de un nodo específico
nodo_busqueda = 7
profundidad_nodo = calcular_profundidad(raiz, nodo_busqueda)

if profundidad_nodo != -1:
    print(f'La profundidad del nodo {nodo_busqueda} es: {profundidad_nodo}')
else:
    print(f'El nodo {nodo_busqueda} no se encuentra en el árbol.')
