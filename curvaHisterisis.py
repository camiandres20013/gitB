import matplotlib.pyplot as plt
import numpy as np

# Definimos los puntos de la curva ascendente
x1 = np.linspace(0, 100, 100)
y1 = (x1-5)**2
x2 = np.linspace(0, 100, 100)
y2 = -(x2-5)**2

plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'b')

# Agregamos títulos y etiquetas de los ejes
plt.title('Gráfica de una curva con histéresis')
plt.xlabel('Magnitud física')
plt.ylabel('Salida o lectura del sensor')

# Mostramos la gráfica
plt.grid()
plt.show()