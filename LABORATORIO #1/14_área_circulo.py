
import math #importamos la libreria para utilizar el numero PI

radio = float(input("Ingresa el radio del círculo: "))# radio del usuario

area_circulo = math.pi * radio**2 # Calcular el área del círculo

print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")
