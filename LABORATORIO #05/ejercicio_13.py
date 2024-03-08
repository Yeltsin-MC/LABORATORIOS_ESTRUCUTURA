"""Comprobar palíndromos: 
Utilizar una pila para comprobar si una palabra o frase es un palíndromo. """

class ComprobadorPalindromo:
    # inicializa el comprobador con una pila vacía
    def __init__(self):
        self.pila = []

    # agrega un caracter a la pila
    def agregar_caracter(self, caracter):
        self.pila.append(caracter)

    # verifica si la palabra o frase es un palíndromo
    def es_palindromo(self, palabra):
        # convierte la palabra a minúsculas y elimina espacios en blanco
        palabra = palabra.lower().replace(" ", "")

        # recorre los caracteres de la palabra y los agrega a la pila
        for caracter in palabra:
            self.agregar_caracter(caracter)

        # compara los caracteres de la pila con los de la palabra en orden inverso
        for caracter in reversed(palabra):
            if caracter != self.pila.pop():
                return False

        # si la pila está vacía, la palabra es un palíndromo
        return len(self.pila) == 0


# ejemplo de uso
if __name__ == "__main__":
    comprobador = ComprobadorPalindromo()

    # solicita al usuario ingresar la palabra o frase a comprobar
    entrada = input("Ingrese una palabra o frase para comprobar si es un palíndromo: ")
    
    if comprobador.es_palindromo(entrada):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
