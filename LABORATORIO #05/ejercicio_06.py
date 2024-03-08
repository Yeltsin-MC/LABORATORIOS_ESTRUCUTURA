"Utilizar una pila para invertir el orden de los caracteres de una cadena."

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


def invertir_cadena(cadena):
    pila = Pila()
    for elemento in cadena:
        pila.apilar(elemento)

    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida


cadena1 = "estrucura de datos"
cadena_invertida = invertir_cadena(cadena1)
print(cadena1)
print(cadena_invertida)
