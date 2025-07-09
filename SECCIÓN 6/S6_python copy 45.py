import matplotlib.pyplot as plt
import numpy as np

# Activamos el modo oscuro antes de graficar
plt.style.use('dark_background')

ypoints = np.array([3, 8, 1, 10, 5, 7])

# Dibujamos la línea y los puntos con un color claro
plt.plot(ypoints, color='cyan', marker='*:r', linewidth=2)

plt.title("Gráfica con marcadores", color='white')
plt.xlabel("Eje X", color='white')
plt.ylabel("Eje Y", color='white')
plt.tick_params(colors='white')

plt.show()
