"""invertir Lista_ Implementa una función que invierta el orden de una lista enlazada simple"""

# definimos la clase nodo para representar los elementos de la lista enlazada
class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# definimos la clase lista_enlazada que contiene métodos para manipular la lista
class lista_enlazada:
    def __init__(self):
        # inicializamos la cabeza de la lista como nula
        self.cabeza = None

    # método para insertar un nuevo nodo al final de la lista
    def insertar_al_final(self, dato):
        nuevo_nodo = nodo(dato)
        # si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            # recorremos la lista hasta encontrar el último nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # método para imprimir los elementos de la lista
    def imprimir_lista(self):
        actual = self.cabeza
        # recorremos la lista e imprimimos cada elemento
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # método para invertir el orden de la lista
    def invertir_lista(self):
        previo = None
        actual = self.cabeza
        siguiente = None

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente

        self.cabeza = previo

# ejemplo de uso
if __name__ == "__main__":
    lista = lista_enlazada()
    lista.insertar_al_final(1)
    lista.insertar_al_final(2)
    lista.insertar_al_final(3)
    lista.insertar_al_final(4)

    print("lista original:")
    lista.imprimir_lista()

    # verifica si la lista no está vacía
    if lista.lista_no_vacia():
        print("\nLa lista no está vacía.")
    else:
        print("\nLa lista está vacía.")
    
    lista.invertir_lista()

    print("\nlista invertida:")
    lista.imprimir_lista()
