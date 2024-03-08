
numero = int(input("Ingresa un número entero: "))

numero_absoluto = abs(numero) # Convertir el número a su valor absoluto

numero_str = str(numero_absoluto) # Convertir el número a una cadena de caracteres



suma_digitos = 0 # es el sumador
for digito_str in numero_str:# Iteramos cada dígito en la cadena

    digito = int(digito_str)
    suma_digitos += digito

print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
