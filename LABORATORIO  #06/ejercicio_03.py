"Desarrolla un programa que encuentre el camino más corto a través de un laberinto."
"Utiliza una cola para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino."

from collections import deque

# Definir laberinto como una matriz de 0s y 1s, donde 0 representa un camino bloqueado y 1 representa un camino válido.
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
]

def bfs(laberinto, inicio, destino):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    visitado = [[False] * columnas for _ in range(filas)]
    cola = deque([(inicio[0], inicio[1], 0)])
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos posibles: derecha, izquierda, abajo, arriba

    while cola:
        x, y, distancia = cola.popleft()
        if (x, y) == destino:
            return distancia
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 1 and not visitado[nx][ny]:
                visitado[nx][ny] = True
                cola.append((nx, ny, distancia + 1))
    
    return -1  # No se encontró un camino válido

# Ejemplo de uso
inicio = (0, 0)
destino = (4, 4)
distancia = bfs(laberinto, inicio, destino)
if distancia != -1:
    print(f"La distancia mínima desde el punto de inicio hasta el destino es: {distancia}")
else:
    print("No se encontró un camino válido desde el punto de inicio hasta el destino en el laberinto.")
