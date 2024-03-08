
"Eliminar los elementos duplicados de una pila."

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


def eliminar_duplicados(pila):
    elementos_unicos = set()

    while not pila.esta_vacia():                  # los elementos de la pila y agregarlos al conjunto si no están presentes
        elemento = pila.desapilar()
        elementos_unicos.add(elemento)
 
    while not pila.esta_vacia():                  # Vaciar la pila original
        pila.desapilar()
    
    for elemento in elementos_unicos:             # Apilar los elementos únicos de nuevo en la pila original
        pila.apilar(elemento)


mi_pila = Pila()
mi_pila.apilar(3)
mi_pila.apilar(1)
mi_pila.apilar(2)
mi_pila.apilar(3)
mi_pila.apilar(1)

print(mi_pila.items)
eliminar_duplicados(mi_pila)
print("Pila sin elementos duplicados:", mi_pila.items)