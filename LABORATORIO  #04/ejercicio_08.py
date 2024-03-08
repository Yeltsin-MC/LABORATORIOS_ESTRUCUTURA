"""8. Validar el estado de una variable después de una operación. 
"""

# inicializamos una variable
mi_variable = 10

# realizamos alguna operación que modifica el estado de la variable
mi_variable *= 2  # por ejemplo, multiplicamos la variable por 2

# validamos el estado de la variable después de la operación
if mi_variable == 20:  # ajusta este valor según la operación realizada
    print("La variable tiene el estado esperado después de la operación.")
else:
    print("La variable no tiene el estado esperado después de la operación.")
