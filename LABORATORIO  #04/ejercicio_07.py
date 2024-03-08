#7. Asegurar que una función retorna un valor específico.

def funcion_especifica(parametro):
    # realizamos operaciones o lógica dentro de la función
    
    # al final de la función, aseguramos que retorne un valor específico
    return 42  # el valor específico que deseas retornar

# ejemplo de uso
resultado = funcion_especifica("algun_parametro")

# verificamos que la función haya retornado el valor específico
if resultado == 42:
    print("La función ha retornado el valor específico.")
else:
    print("La función no ha retornado el valor específico.")
