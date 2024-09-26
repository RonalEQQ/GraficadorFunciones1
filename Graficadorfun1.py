import numpy as np
import matplotlib.pyplot as plt
import math

# Definir un diccionario con funciones matemáticas comunes para usarlas sin 'np.'
funciones_permitidas = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'log': np.log,
    'exp': np.exp,
    'sqrt': np.sqrt,
    'pi': np.pi,
    'e': np.e
}

# Solicitar la función al usuario
funcion_usuario = input("Ingresa la función en términos de x (por ejemplo: sin(x) + 0.5*x): ")

# Reemplazar funciones comunes para que el usuario no tenga que escribir 'np.'
def f(x):
    # 'eval' utilizará las funciones del diccionario 'funciones_permitidas'
    return eval(funcion_usuario, {"_builtins_": None, "x": x, **funciones_permitidas})

# Definir el rango de x
x = np.linspace(-10, 10, 400)

# Calcular la función ingresada
y = f(x)

# Graficar la función
plt.plot(x, y, label=f'f(x) = {funcion_usuario}')

# Añadir etiquetas y leyenda
plt.title("Gráfica de la función ingresada")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()