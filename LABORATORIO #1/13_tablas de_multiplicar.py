
# Obtener el número del usuario
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11): #ponemos el límite
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
