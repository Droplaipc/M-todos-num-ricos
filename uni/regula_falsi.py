# Método de regula falsi
import math as m
import numpy as np

# Función
def f(t):
    # retornar regla de correspondencia
    return m.exp(t) + t

# Intervalo
a = -1
b = 0

# Número de iteraciones
n = 5

# Evaluar la función en ambos extremos
fa = f(a)
fb = f(b)

# Verificar la condición de Bolzano
if fa * fb < 0:

    # Bucle iterador
    for _ in range(n):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(x)*f(a) < 0:
            b = x
        elif f(x)*f(b) < 0:
            a = x

    print(f"la raíz para {n} iteraciones es {x}")

elif fa * fb > 0:
    print("Los extremos del intervalo no cumplen la condición de Bolzano\n"
          "No puede aplicarse el método de la bisección.")
else:
    print("La raíz es: ", a if fa == 0 else b)