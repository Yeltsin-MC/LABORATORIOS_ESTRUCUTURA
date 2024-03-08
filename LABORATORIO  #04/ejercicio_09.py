"""9. Asegurar que un módulo se ha importado correctamente. 
"""

import importlib


try:
    # intentamos importar el módulo deseado
    importlib
    
    # si la importación tiene éxito, mostramos un mensaje indicando que se ha importado correctamente
    print("El módulo se ha importado correctamente.")
except ImportError:
    # si hay un error al importar, mostramos un mensaje de error
    print("Hubo un error al importar el módulo.")
