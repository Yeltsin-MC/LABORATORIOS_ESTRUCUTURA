"Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila."


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
    
    def ultimo_elemento(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print("la pila esta vacia")

def verificar_anidacion(expresion):
    pila = Pila()
    operadores_abiertos = "([{"
    operadores_cerrados = ")]}"

    for caracter in expresion:
        if caracter in operadores_abiertos:
            pila.apilar(caracter)
        elif caracter in operadores_cerrados:
            operador_cerrado = caracter
            operador_abierto = pila.desapilar()
            if operador_abierto is None or operadores_abiertos.index(operador_abierto) != operadores_cerrados.index(operador_cerrado):
                return False
    return pila.esta_vacia()



expresion1 = "((3 + 2) * 5)"
expresion2 = "((3 + 2) * 5"

anidado1 = verificar_anidacion(expresion1)
anidado2 = verificar_anidacion(expresion2)

print(anidado1)
print(anidado2)