"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
comienzan con una letra determinada"""

def buscador(list,x): # buscador sefun la inicial
    lista2=set()     #creamos el conjunto set
    for i in list: #iterador de elelemtos
        for j in i:
            
            if j ==x:
                lista2.add(i)
    return lista2

letra=str(input("Con que letra quiere buscar? :"))    #damos un conjunto
conjunto={'juan','ana','maria','sofi','sefa','kati'}
resultado=buscador(conjunto,letra)                     #pasamos datos a la función
print(resultado)