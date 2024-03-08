"Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales."

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
           return self.items.pop()
        else:
            print("la pila esta vacia")

def ordenar_pila_ascendente(pila):
    lista = []                                      #   los elementos de la pila y almacénalos en una lista
    while not pila.esta_vacia():
        lista.append(pila.desapilar())

    lista.sort()                                    #  Ordena la lista en orden ascendente

    for elemento in lista:                          # los elementos ordenados de la lista y apílalos de nuevo en la pila original
        pila.apilar(elemento)



mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(3)
mi_pila.apilar(1)
mi_pila.apilar(4)
mi_pila.apilar(2)

print(mi_pila.items)

ordenar_pila_ascendente(mi_pila)

print("Pila ordenada de manera ascendente:", mi_pila.items)