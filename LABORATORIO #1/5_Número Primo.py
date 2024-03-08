"Verifica si un número ingresado por el usuario es primo o no"

numero = int(input("Ingresar un número para verificar si es primo: "))

def es_primo(numero):   #va calcular si es numero es primo o no
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

if es_primo(numero):            #imprime en caso sea un primo
    print(f"{numero} es un número primo")
else:                                   #imprime en caso no sea un primo
    print(f"{numero} no es un número primo.")