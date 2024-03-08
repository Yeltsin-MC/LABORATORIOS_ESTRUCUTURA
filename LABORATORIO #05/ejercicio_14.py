"""Simular el proceso de deshacer (undo): 
Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
deshaceres. """

class SistemaUndo:
    def __init__(self):
        # Pila para acciones realizadas
        self.pila_acciones = []
        # Pila para deshacer acciones
        self.pila_deshacer = []

    def realizar_accion(self, accion):
        # Realiza una acción y la agrega a la pila de acciones
        print(f"Realizando acción: {accion}")
        self.pila_acciones.append(accion)
        # Al realizar una nueva acción, la pila de deshacer se reinicia
        self.pila_deshacer = []

    def deshacer_accion(self):
        # Verifica si hay acciones para deshacer
        if not self.pila_acciones:
            print("No hay acciones para deshacer.")
            return

        # Obtiene la última acción realizada
        ultima_accion = self.pila_acciones.pop()
        # Agrega la acción deshecha a la pila de deshacer
        self.pila_deshacer.append(ultima_accion)

        print(f"Deshaciendo acción: {ultima_accion}")

    def rehacer_accion(self):
        # Verifica si hay acciones para rehacer
        if not self.pila_deshacer:
            print("No hay acciones para rehacer.")
            return

        # Obtiene la última acción deshecha
        ultima_accion_deshacer = self.pila_deshacer.pop()
        # Realiza la acción nuevamente y la agrega a la pila de acciones
        print(f"Rehaciendo acción: {ultima_accion_deshacer}")
        self.pila_acciones.append(ultima_accion_deshacer)

# Ejemplo de uso
if __name__ == "__main__":
    sistema_undo = SistemaUndo()

    # Realizar algunas acciones
    sistema_undo.realizar_accion("Escribir texto")
    sistema_undo.realizar_accion("Eliminar elemento")
    sistema_undo.realizar_accion("Modificar configuración")

    # Deshacer la última acción
    sistema_undo.deshacer_accion()

    # Realizar una nueva acción después de deshacer
    sistema_undo.realizar_accion("Agregar elemento")

    # Rehacer la acción deshecha
    sistema_undo.rehacer_accion()
