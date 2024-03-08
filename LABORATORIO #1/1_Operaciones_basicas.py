"Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario."


numero1 = float(input("ingrese un numero: ")) # solicita al usuario ingresar dos números
numero2 = float(input("ingrese un numero: "))

# realiza operaciones matemáticas con los números ingresados
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# redondea el resultado a dos decimales
division = round(numero1 / numero2, 2)

# imprime los resultados 
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicación: {multiplicacion}")
print(f"división: {division}")
