"Crea una función que calcule la factorial de un número"

número = int(input("Ingrese un número entero :"))       #pide un número
factorial = 1
for contador in range(1,número):          #itera para calcular el factorial

    factorial += factorial* contador


print(factorial)