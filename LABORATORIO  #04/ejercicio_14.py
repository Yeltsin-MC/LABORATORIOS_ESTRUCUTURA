"""Eliminar Duplicados 
14. Crea una función que elimine los nodos duplicados de una lista enlazada simple."""
# definimos la clase nodo para representar los elementos de la lista enlazada
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

    # Método para imprimir los eleementos de la lista
    def imprimir_lista(self):
        actual = self.cabeza
        # Recorremos la lista e imprimimos cada elemento
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método para eliminar los nodos duplicados de la lista
    def eliminar_duplicados(self):
        valores_unicos = set()  # Utilizamos un conjunto para rastrear los valores únicos
        actual = self.cabeza
        previo = None

        while actual:
            if actual.dato in valores_unicos:
                # Si el valor ya está en el conjunto, es un duplicado y lo eliminamos
                previo.siguiente = actual.siguiente
            else:
                # Si es un valor único, lo agregamos al conjunto
                valores_unicos.add(actual.dato)
                previo = actual

            actual = actual.siguiente

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertar_al_final(1)
    lista.insertar_al_final(2)
    lista.insertar_al_final(3)
    lista.insertar_al_final(2)
    lista.insertar_al_final(4)

    print("Lista original:")
    lista.imprimir_lista()

    lista.eliminar_duplicados()

    print("\nLista sin duplicados:")
    lista.imprimir_lista()

