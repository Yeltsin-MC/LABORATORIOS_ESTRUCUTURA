"""Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el
primero y viceversa) e imprime la lista hacia adelante y hacia atrás"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato  # creamos un nuevo nodo
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

    def eliminar_nodos_duplicados(self):
        datos_vistos = set()
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato not in datos_vistos:
                datos_vistos.add(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente
            else:
                nodo_siguiente = nodo_actual.siguiente
                self.eliminar_nodo(nodo_actual)
                nodo_actual = nodo_siguiente

    def eliminar_nodo(self, nodo):
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.primero = nodo.siguiente
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.ultimo = nodo.anterior

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

# Insertar nodos en la lista con datos duplicados
for dato in [1, 2, 3, 2, 4, 5, 3, 6, 7]:
    lista.insertar_al_final(dato)

print("Lista original hacia adelante:")
lista.imprimir_adelante()

print("Lista original hacia atrás:")
lista.imprimir_atras()

# Eliminar nodos duplicados
lista.eliminar_nodos_duplicados()

print("\nLista sin nodos duplicados hacia adelante:")
lista.imprimir_adelante()

print("Lista sin nodos duplicados hacia atrás:")
lista.imprimir_atras()
