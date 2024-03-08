
#Escriba una función que reciba un conjunto de números
# y devuelva un conjunto con los números que son divisibles por un número determinado.

def numero(conjunto, divisor):          #en este caso toma 2 argumentos
   
    divisibles = {num for num in conjunto if num % divisor == 0}       #Nos devolveras los numeros que son divisibles por el divisor
    return divisibles


conjunto_numeros = {4,8,5,10,20,15,13}              #ejemplo
divisor = 5

numeros_divisibles = numero(conjunto_numeros, divisor)

print(conjunto_numeros)
print(numeros_divisibles)



