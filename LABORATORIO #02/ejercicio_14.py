"""Calcula la media, la mediana y la desviación estándar de los elementos de una matriz."""

import statistics     #importamos este modulo ya que es una pregunta de estadistica

# Definir una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

todos_los_elementos = [elemento for fila in matriz for elemento in fila]  # intera la matriz para obtener los elementos 

                                                                        # Calcular la media, mediana y desviacion estandar
media= sum(todos_los_elementos) / len(todos_los_elementos)
mediana= statistics.median(todos_los_elementos)
desviacion_estandar = statistics.stdev(todos_los_elementos)

print("Matriz:")
for fila in matriz:
    print(fila)     #imprime la fila y así toda la matriz

print("\nMedia de los elementos de la matriz:", media)           #imprimen los resusltados
print("Mediana de los elementos de la matriz:", mediana)
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)