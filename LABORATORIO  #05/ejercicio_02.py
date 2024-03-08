"""Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato
impar e imprime la lista hacia adelante y hacia atrás"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # # creamos un nuevo nodo
        self.siguiente = None  # siguiente nodo
        self.anterior = None  # referencia al nodo anterior

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None  # primer nodo 
        self.ultimo = None  # último nodo 

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:  # si la lista está vacía
            self.primero = nuevo_nodo  # el nuevo nodo es el primero
            self.ultimo = nuevo_nodo  # y también es el último
        else:
            nuevo_nodo.anterior = self.ultimo  # el nodo anterior al nuevo nodo es el último actual
            self.ultimo.siguiente = nuevo_nodo  # el siguiente del último actual es el nuevo nodo
            self.ultimo = nuevo_nodo  # el nuevo nodo ahora es el último

    def contar_pares_impares(self):
        nodo_actual = self.primero
        pares = 0
        impares = 0
        while nodo_actual:
            if nodo_actual.dato % 2 == 0:  # si el dato del nodo es par
                pares += 1  # incrementar el contador de pares
            else:
                impares += 1  # de lo contrario, incrementar el contador de impares
            nodo_actual = nodo_actual.siguiente  # pasar al siguiente nodo
        return pares, impares  # devolver la cantidad de pares e impares

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
for dato in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    lista.insertar_al_final(dato)

print("Lista hacia adelante:")
lista.imprimir_adelante()

print("Lista hacia atrás:")
lista.imprimir_atras()

# Contar nodos pares e impares
pares, impares = lista.contar_pares_impares()
print(f"\nNodos pares: {pares}, Nodos impares: {impares}")
