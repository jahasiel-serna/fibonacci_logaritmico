import numpy as np

def fibonacci(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return fibonacci(np.dot(x,x), n//2)
    return np.dot(x, fibonacci(x, n-1))

F = np.array([[0,1],[1,1]], dtype=object)
n = int(input("Número de la sucesión: "))
F = fibonacci(F, n-1)
print("F(",n,") =", F[1][1])