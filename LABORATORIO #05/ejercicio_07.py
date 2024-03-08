"Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila."

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
            
def decimal_a_binario(decimal):
    pila = Pila()

    while decimal > 0:                                        # Convertir el decimal a binario usando el algoritmo de división sucesiva
        residuo = decimal % 2
        pila.apilar(residuo)
        decimal //= 2

 
    binario = ""                                                 # Construir la representación binaria a partir de los elementos de la pila
    while not pila.esta_vacia():
        binario += str(pila.desapilar())             

    return binario


# Pedir al usuario que ingrese un número decimal
numero = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = decimal_a_binario(numero)
print(numero)
print(binario)