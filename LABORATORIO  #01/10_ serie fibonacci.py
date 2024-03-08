def fibonacci(n): # Función para generar los N Fibonacci
    fib_series = [] #creamos la lista
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a) #agregamos a la lista
        a, b = b, a + b

    return fib_series

primeros_10_fibonacci = fibonacci(10) #pedimos los primeros 10 números de la serie Fibonacci


print("Los primeros 10 números de la serie Fibonacci:", primeros_10_fibonacci)
