"Solicita un número al usuario y determina si es par o impar."

usuario = float(input("Ingrese un numero: ")) # solicita al usuario ingresar un número

if usuario % 2 == 0: # verifica si el número ingresado es par o impar
    print(f"{usuario} es un número par.")
else:
    print(f"{usuario} es un número impar.")
    