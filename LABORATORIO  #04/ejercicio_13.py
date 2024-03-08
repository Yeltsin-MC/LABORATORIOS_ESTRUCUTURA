# Definimos la clase Nodo para representar los elementos de la lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definimos la clase ListaEnlazada que contiene métodos para manipular la lista
class ListaEnlazada:
    def __init__(self):
        # Inicializamos la cabeza de la lista como nula
        self.cabeza = None

    # Método para insertar un nuevo nodo al final de la lista
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            # Recorremos la lista hasta encontrar el último nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para imprimir los elementos de la lista
    def imprimir_lista(self):
        actual = self.cabeza
        # Recorremos la lista e imprimimos cada elemento
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método para concatenar dos listas enlazadas
    def concatenar_listas(self, otra_lista):
        actual = self.cabeza
        # Recorremos la lista hasta encontrar el último nodo
        while actual.siguiente:
            actual = actual.siguiente
        # Establecemos el siguiente del último nodo de la primera lista al primero de la segunda lista
        actual.siguiente = otra_lista.cabeza

# Ejemplo de uso
if __name__ == "__main__":
    lista1 = ListaEnlazada()
    lista1.insertar_al_final(1)
    lista1.insertar_al_final(2)
    lista1.insertar_al_final(3)

    lista2 = ListaEnlazada()
    lista2.insertar_al_final(4)
    lista2.insertar_al_final(5)

    print("Lista 1:")
    lista1.imprimir_lista()

    print("\nLista 2:")
    lista2.imprimir_lista()

    lista1.concatenar_listas(lista2)

    print("\nListas concatenadas:")
    lista1.imprimir_lista()
