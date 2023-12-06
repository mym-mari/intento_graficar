import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Función para generar datos en tiempo real (puedes sustituir esto con tus propios datos en tiempo real)
def generar_datos():
    return np.random.rand()

# Inicializar la figura y el eje
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], lw=2)

# Configurar el eje
ax.set_xlim(0, 10)  # Puedes ajustar estos límites según tus necesidades
ax.set_ylim(0, 1)

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización para la animación en tiempo real
def update(frame):
    x_data.append(frame)
    y_data.append(generar_datos())
    line.set_data(x_data, y_data)
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 200), init_func=init, blit=True)

# Mostrar la gráfica en una ventana
plt.show()
