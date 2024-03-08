"""Implementar una calculadora sencilla: 
Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
expresiones. """
class calculadora:
    # inicializa la calculadora con una pila vacía
    def __init__(self):
        self.pila = []

    # verifica si un token es un número
    def es_operando(self, token):
        return token.isdigit()

    # realiza la operación correspondiente según el operador
    def realizar_operacion(self, operador):
        try:
            operando2 = self.pila.pop()
            operando1 = self.pila.pop()

            # realiza la operación y guarda el resultado en la pila
            if operador == '+':
                resultado = operando1 + operando2
            elif operador == '-':
                resultado = operando1 - operando2
            elif operador == '*':
                resultado = operando1 * operando2
            elif operador == '/':
                resultado = operando1 / operando2
            else:
                raise ValueError("Operador no válido")

            self.pila.append(resultado)
        except IndexError:
            raise ValueError("Expresión no válida")

    # evalúa la expresión dada utilizando la pila
    def evaluar_expresion(self, expresion):
        tokens = expresion.split()

        # recorre los tokens de la expresión
        for token in tokens:
            # si es un número, lo agrega a la pila
            if self.es_operando(token):
                self.pila.append(float(token))
            else:
                # si es un operador, realiza la operación correspondiente
                self.realizar_operacion(token)

        # si la pila tiene un solo elemento, es el resultado
        if len(self.pila) == 1:
            return self.pila[0]
        else:
            raise ValueError("Expresión no válida")


# ejemplo de uso
if __name__ == "__main__":
    calc = calculadora()

    # solicita al usuario ingresar la expresión matemática
    expresion = input("Ingrese la expresión matemática: ")
    
    try:
        resultado = calc.evaluar_expresion(expresion)
        # imprime el resultado
        print(f"Resultado: {resultado}")
    except ValueError as e:
        # maneja errores e imprime el mensaje correspondiente
        print(f"Error: {e}")
