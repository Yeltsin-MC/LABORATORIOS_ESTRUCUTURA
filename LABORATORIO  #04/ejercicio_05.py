#5. Validar la igualdad de dos objetos.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # método para sobrecargar el operador de igualdad (==)
    def __eq__(self, otra_persona):
        # verifica si el nombre y la edad son iguales
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

# ejemplo de uso
if __name__ == "__main__":
    # creamos dos objetos de la clase Persona
    persona1 = Persona("Juan", 25)
    persona2 = Persona("Maria", 30)
    persona3 = Persona("Juan", 25)

    # comparamos los objetos utilizando el operador de igualdad
    if persona1 == persona2:
        print("Las personas son iguales.")
    else:
        print("Las personas son diferentes.")

    if persona1 == persona3:
        print("Las personas son iguales.")
    else:
        print("Las personas son diferentes.")
