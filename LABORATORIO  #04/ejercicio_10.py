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

    # Método para buscar un nodo con un valor específico en la lista
    def buscar_nodo(self, valor):
        actual = self.cabeza

        # Recorremos la lista hasta encontrar el nodo con el valor deseado
        while actual:
            if actual.dato == valor:
                return actual  # Devolvemos el nodo si encontramos el valor
            actual = actual.siguiente

        return None  # Devolvemos None si no encontramos el valor en la lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertar_al_final(1)
    lista.insertar_al_final(2)
    lista.insertar_al_final(3)

    print("Lista:")
    lista.imprimir_lista()

    valor_a_buscar = 2
    nodo_encontrado = lista.buscar_nodo(valor_a_buscar)

    if nodo_encontrado:
        print(f"\nNodo con el valor {valor_a_buscar} encontrado en la lista.")
    else:
        print(f"\nNodo con el valor {valor_a_buscar} no encontrado en la lista.")
