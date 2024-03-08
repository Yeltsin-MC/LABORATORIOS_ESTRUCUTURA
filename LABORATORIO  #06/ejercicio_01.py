"Implementa una función que determine si una palabra es palíndroma o no."
"Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso."

class Cola:
    def __init__(self):
        # inicializa una cola vacía usando una lista
        self.items = []

    def encolar(self, item):
        # añade un elemento al principio de la cola (posición 0 de la lista)
        self.items.insert(0, item)

    def desencolar(self):
        # elimina y devuelve el elemento al final de la cola
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        # verifica si la cola está vacía
        return self.items == []


def es_palindroma(palabra):
    # crea una instancia de la clase Cola
    cola = Cola()

    # encola cada letra de la palabra en la cola
    for letra in palabra:
        cola.encolar(letra)

    palabra_reversa = ''

    # desencola cada letra de la cola y construye la palabra reversa
    while not cola.esta_vacia():
        palabra_reversa += cola.desencolar()

    # verifica si la palabra original es igual a la palabra reversa
    return palabra == palabra_reversa


# ejemplo de uso
palabra = "reconocer"
if es_palindroma(palabra):
    print(f"{palabra} es palíndroma")
else:
    print(f"{palabra} no es palíndroma")
