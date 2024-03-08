"Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos."

def primo(numero):  #definimos si el numero es primo
    
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  #itera desde 2 hasta la raíz cuadrada de 'numero' + 1
        if numero % i == 0: # si el numero es dibisible por "i"
            return False
    return True

def numeros_primos(conjunto):            #definimos para que nos devuelva los numeros primos del conjunto

    primos = {numero for numero in conjunto if primo(numero)} #devueleve
    return primos

conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15}
conjunto_primos = numeros_primos(conjunto_numeros)

print(conjunto_numeros)
print(conjunto_primos)
