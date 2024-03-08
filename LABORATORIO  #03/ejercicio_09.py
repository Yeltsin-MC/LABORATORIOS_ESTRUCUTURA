#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada.



def palabras_longitud(conjunto_palabras, longitud):            #definimos para que nos debuelva palabras con la longitud deseada
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}       #iteramos la palabra en el conjunto 
                                                                                                         #y seleccionamos con la longitud deseado
    return palabras_seleccionadas


conjunto_palabras = {"estructura", "python", "programacion", "peru", "quinn", "ciencia"}            #ejemplo
longitud_deseada = 5

resultado = palabras_longitud(conjunto_palabras, longitud_deseada)

print(conjunto_palabras)
print(resultado)
