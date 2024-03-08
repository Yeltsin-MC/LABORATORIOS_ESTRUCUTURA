#3. Validar el rango de una calificación.
def validar_edad():
    try:
        edad = int(input("Ingrese su edad: "))
        assert edad >= 0, "La edad no puede ser un número negativo."
        
        if edad < 18:
            print("Eres menor de edad.")
        else:
            print("Eres mayor de edad.")
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese un número entero válido.")
    except AssertionError as e:
        print(f"Error: {e}")

# Llamamos a la función para probarla
validar_edad()