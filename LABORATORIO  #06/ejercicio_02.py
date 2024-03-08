"Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que fueron recibidos."
"Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado actual de la cola."

class ColaPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def procesar_pedido(self):
        if self.pedidos:
            pedido_procesado = self.pedidos.pop(0)
            print(f"Procesando pedido: {pedido_procesado}")
        else:
            print("No hay pedidos para procesar")

    def mostrar_estado(self):
        if self.pedidos:
            print("Estado actual de la cola de pedidos:")
            for pedido in self.pedidos:
                print(pedido)
        else:
            print("La cola de pedidos está vacía")


# Ejemplo de uso
cola_pedidos = ColaPedidos()

# Agregar algunos pedidos
cola_pedidos.agregar_pedido("Pedido 1: Pizza")
cola_pedidos.agregar_pedido("Pedido 2: Hamburguesa")
cola_pedidos.agregar_pedido("Pedido 3: Ensalada")

# Mostrar el estado actual de la cola
cola_pedidos.mostrar_estado()

# Procesar los pedidos en el orden en que fueron recibidos
cola_pedidos.procesar_pedido()
cola_pedidos.procesar_pedido()
cola_pedidos.procesar_pedido()
cola_pedidos.procesar_pedido()

# Mostrar el estado actual de la cola después de procesar los pedidos
cola_pedidos.mostrar_estado()
