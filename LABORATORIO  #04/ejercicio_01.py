#. Validar la edad de un usuario.

def val_edad(edad):
    if edad < 0:            #raise es para generar  manuealmente excepciones
        raise ValueError("La edad no puede ser un número negativo.")
    elif edad < 18:
        print("Eres menor de edad.")
    elif edad >100:
        raise ValueError("La edad no creo supere 100 años actualmente.")

    else:
        print("Eres mayor de edad.")

try:
    edad_u = int(input("Ingrese su edad: "))
    val_edad(edad_u)
except ValueError as error:
    print(f"Error: {error}. Por favor, ingrese un número entero válido.")
