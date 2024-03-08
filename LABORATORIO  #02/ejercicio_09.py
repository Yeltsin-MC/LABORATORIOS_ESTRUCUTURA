"""Accede al elemento central de una matriz"""

print("para ser poder acceder al elemento central, la matris tiene que ser de longitus impar, MxN M=N , impar")

import random        # importamos el modulo random 
A = []       #creaos una lista basia


def pedir_f():                                                         # funcion para pedir al usuario el numero de filas
    filas = int(input("Digite el tamaño de la matris (impar):"))
    return filas


def llenar_mostrar(matriz):        # función que va crear la matris               
    filas = pedir_f()           #se llama a la funcion pedir_f
    for i in range(filas):
        matriz.append([])       #esto hace que agregue una nueva fila
        for j in range(filas):
            matriz[i].append(random.randint(1, 10))        # va iterar las N veces que pusimos agregando un numero random
    print("matriz A")

    for row in matriz: # va imprimir fila por fila
        print(row)

def encontrar_elemento_central(matriz):  #funcion que ubicará al elemento central
    filas = len(matriz)  #lees cuanot elementos hay
    fila_central = filas // 2        #hace divicion entera y el resultado es el indice en la fila (como empiea en INDICE 0)

    columna_central = filas // 2         #hace divicion entera y el resultado es el indice en la columna (como empiea en INDICE 0)

    elemento_central = matriz[fila_central][columna_central]      #busca al elemeto central
    print(f"El elemento central de la matriz es: {elemento_central}")


llenar_mostrar(A)                 #llamamos a la función
encontrar_elemento_central(A)    #llamamos a la función

