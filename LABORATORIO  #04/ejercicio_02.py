"Verificar el tipo de dato de una variable"

def verificar_tipo(variable, tipo_esperado): #    Función para verificar si una variable tiene el tipo esperado.

    assert isinstance(variable, tipo_esperado), f"Error: Se esperaba un {tipo_esperado} pero se encontró {type(variable)}."

# Ejemplo de uso:
variable_1 = 5
variable_2 = "Hola"
variable_3 = [1, 2, 3]

verificar_tipo(variable_1, int)  
verificar_tipo(variable_2, str)  
verificar_tipo(variable_3, dict) 
