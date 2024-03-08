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

    # Método para obtener la longitud de la lista
    def longitud_lista(self):
        longitud = 0
        actual = self.cabeza

        # Recorremos la lista y contamos cada nodo
        while actual:
            longitud += 1
            actual = actual.siguiente

        return longitud

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertar_al_final(1)
    lista.insertar_al_final(2)
    lista.insertar_al_final(3)

    print("Lista:")
    lista.imprimir_lista()

    longitud = lista.longitud_lista()
    print(f"\nLongitud de la lista: {longitud}")
