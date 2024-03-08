"""Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista
duplicada hacia adelante y hacia atrás.
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # # creamos un nuevo nodo
        self.siguiente = None  #  siguiente nodo
        self.anterior = None  #  nodo anterior

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None  # primer nodo de la lista
        self.ultimo = None  # último nodo de la lista

    def insertar_al_final(self, dato):
        # Crear un nuevo nodo con el dato proporcionado
        nuevo_nodo = Nodo(dato)
        if not self.primero:
            # Si la lista está vacía, el nuevo nodo es tanto el primero como el último
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            # Si la lista no está vacía, añadir el nuevo nodo al final
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def duplicar_nodos(self):
        nodo_actual = self.primero
        while nodo_actual:
            # Crear un nuevo nodo con el mismo dato del nodo actual
            nuevo_nodo = Nodo(nodo_actual.dato)
            # Configurar las referencias del nuevo nodo y el nodo actual
            nuevo_nodo.siguiente = nodo_actual.siguiente
            nuevo_nodo.anterior = nodo_actual
            if nodo_actual.siguiente:
                nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo
            # Avanzar al siguiente par de nodos (original y duplicado)
            nodo_actual = nuevo_nodo.siguiente

    def imprimir_adelante(self):
        # Imprimir los nodos en orden desde el primero hasta el último
        nodo_actual = self.primero
        while nodo_actual:
            print(nodo_actual.dato, end=" ")  # Imprimir el dato del nodo
            nodo_actual = nodo_actual.siguiente
        print()

    def imprimir_atras(self):
        # Imprimir los nodos en orden inverso desde el último hasta el primero
        nodo_actual = self.ultimo
        while nodo_actual:
            print(nodo_actual.dato, end=" ")  # Imprimir el dato del nodo
            nodo_actual = nodo_actual.anterior
        print()

# Ejemplo de uso
lista_original = ListaDoblementeEnlazada()

# Insertar nodos en la lista original
for dato in [1, 2, 3, 4]:
    lista_original.insertar_al_final(dato)

print("lista original hacia adelante:")
lista_original.imprimir_adelante()

print("lista original hacia atrás:")
lista_original.imprimir_atras()

# Duplicar nodos
lista_original.duplicar_nodos()

print("\nlista duplicada hacia adelante:")
lista_original.imprimir_adelante()

print("lista duplicada hacia atrás:")
lista_original.imprimir_atras()
