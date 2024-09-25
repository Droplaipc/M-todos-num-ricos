# Programa general métodos numéricos
import math as m
import numpy as np

# Función
def f(t):
    return m.exp(t) + t

# Derivada de la función
def df(t):
    return m.exp(t) + 1

class NumMethods:

    def __init__(self, n):
        # Número de iteraciones
        self.n = n

    # Método de la biyección/bipartición
    def bipartition(self, a, b):
        # Evaluar la función en ambos extremos
        fa = f(a)
        fb = f(b)

        # Verificar la condición de Bolzano
        if fa * fb < 0:

            # Bucle iterador
            for _ in range(self.n):
                x = (b + a) / 2

                if f(x) * f(a) < 0:
                    b = x
                elif f(x) * f(b) < 0:
                    a = x

            print(f"la raíz para {self.n} iteraciones es {x}")
        return x

    # Método de regula falsi
    def regul_falsi(self, a, b):
        # Evaluar la función en ambos extremos
        fa = f(a)
        fb = f(b)

        # Verificar la condición de Bolzano
        if fa * fb < 0:

            # Bucle iterador
            for _ in range(self.n):
                x = (a * f(b) - b * f(a)) / (f(b) - f(a))

                if f(x) * f(a) < 0:
                    b = x
                elif f(x) * f(b) < 0:
                    a = x

            print(f"la raíz para {self.n} iteraciones es {x}")
        return x

    # Método de Newton-Raphson
    def newton_raph(self, x):

        # Bucle iterador
        for _ in range(self.n):
            x -= f(x)/df(x)

        print(f"la raíz para {self.n} iteraciones es {x}")
        return x

metodos = NumMethods(5)

metodos.bipartition(-1, 0)
metodos.regul_falsi(-1, 0)
metodos.newton_raph(1)
