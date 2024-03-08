"Implementa un sistema de gestión de tareas que permita agregar tareas,"
"marcar tareas como completadas y mostrar la próxima tarea pendiente."

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, indice_tarea):
        if 0 <= indice_tarea < len(self.tareas):
            self.tareas[indice_tarea]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Índice de tarea inválido.")

    def obtener_proxima_tarea_pendiente(self):
        for tarea in self.tareas:
            if not tarea["completada"]:
                return tarea["descripcion"]
        return "No hay tareas pendientes"

    def mostrar_tareas(self):
        print("Lista de tareas:")
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - Estado: {estado}")


# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()

# Agregar algunas tareas
sistema_tareas.agregar_tarea("Lavar los platos")
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Estudiar para el examen")

# Mostrar la próxima tarea pendiente
print("Próxima tarea pendiente:", sistema_tareas.obtener_proxima_tarea_pendiente())

# Marcar la primera tarea como completada
sistema_tareas.marcar_completada(0)

# Mostrar la próxima tarea pendiente después de marcar una como completada
print("Próxima tarea pendiente:", sistema_tareas.obtener_proxima_tarea_pendiente())

# Mostrar todas las tareas y sus estados
sistema_tareas.mostrar_tareas()
