"""Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la
lista hacia adelante y hacia atrás.
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # # creamos un nuevo nodo
        self.siguiente = None  # referencia al siguiente nodo
        self.anterior = None  # referencia al nodo anterior

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None  # primer nodo de la lista
        self.ultimo = None  # último nodo de la lista

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:  # si la lista está vacía
            self.primero = nuevo_nodo  # el nuevo nodo es el primero
            self.ultimo = nuevo_nodo  # y también es el último
        else:
            nuevo_nodo.anterior = self.ultimo  # el nodo anterior al nuevo nodo es el último actual
            self.ultimo.siguiente = nuevo_nodo  # el siguiente del último actual es el nuevo nodo
            self.ultimo = nuevo_nodo  # el nuevo nodo ahora es el último

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion == 1:  # si la posición es 1
            nuevo_nodo.siguiente = self.primero  # el siguiente del nuevo nodo es el primero actual
            self.primero.anterior = nuevo_nodo  # el anterior del primer nodo actual es el nuevo nodo
            self.primero = nuevo_nodo  # el nuevo nodo ahora es el primero
        else:
            nodo_actual = self.primero
            for _ in range(posicion - 2):  # recorrer hasta la posición deseada
                if nodo_actual is not None:
                    nodo_actual = nodo_actual.siguiente
            if nodo_actual is not None:
                nuevo_nodo.anterior = nodo_actual  # el anterior del nuevo nodo es el nodo actual
                nuevo_nodo.siguiente = nodo_actual.siguiente  # el siguiente del nuevo nodo es el siguiente del nodo actual
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nuevo_nodo  # el anterior del siguiente del nodo actual es el nuevo nodo
                nodo_actual.siguiente = nuevo_nodo  # el siguiente del nodo actual es el nuevo nodo

    def imprimir_adelante(self):
        nodo_actual = self.primero
        while nodo_actual:
            print(nodo_actual.dato, end=" ")  # Imprimir el dato del nodo
            nodo_actual = nodo_actual.siguiente  # pasar al siguiente nodo
        print()

    def imprimir_atras(self):
        nodo_actual = self.ultimo
        while nodo_actual:
            print(nodo_actual.dato, end=" ")  # Imprimir el dato del nodo
            nodo_actual = nodo_actual.anterior  # pasar al nodo anterior
        print()

# Ejemplo de uso
lista = ListaDoblementeEnlazada()

# Insertar nodos en la lista
for dato in [1, 2, 3, 4, 5]:
    lista.insertar_al_final(dato)

print("Lista original hacia adelante:")
lista.imprimir_adelante()

print("Lista original hacia atrás:")
lista.imprimir_atras()

# Insertar un nuevo nodo con el dato 15 en la posición 3
lista.insertar_en_posicion(15, 3)

print("\nLista con el nuevo nodo hacia adelante:")
lista.imprimir_adelante()

print("Lista con el nuevo nodo hacia atrás:")
lista.imprimir_atras()
