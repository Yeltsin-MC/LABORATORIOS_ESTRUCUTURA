def contando_vocales(cadena): # Función para contar vocales de la cadena

    contador_vocales = 0     # contador de vocales

    cadena = cadena.lower() #Aquí convertimos las mayuculas minusculas


    for caracter in cadena:  # Iterar sobre cada carácter en la cadena y contamos las N vocales
        if caracter in "aeiou":
            contador_vocales += 1


    return contador_vocales #retorna el resultado final

# Ejemplo de uso
texto = "este es mi primer laboratorio"
numero_vocales = contando_vocales(texto)

# Imprimir el resultado
print("Número de vocales en la cadena:", numero_vocales)
