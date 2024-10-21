Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... # Parámetros de la simulación
... d = 0.0002  # Separación entre las dos rendijas (en metros)
... L = 1.0     # Distancia entre la rendija y la pantalla (en metros)
... wavelength = 500e-9  # Longitud de onda de la luz (en metros, 500 nm)
... 
... # Espacio en el eje X (pantalla)
... x = np.linspace(-0.01, 0.01, 1000)  # Rango de -1 cm a 1 cm
... 
... # Calcula el ángulo theta para cada punto x de la pantalla
... theta = np.arctan(x / L)
... 
... # Calcula la diferencia de fase delta para cada ángulo
... delta = (2 * np.pi / wavelength) * d * np.sin(theta)
... 
... # Intensidad en la pantalla (patrón de interferencia)
... I = (np.cos(delta / 2))**2  # Patrón típico de dos rendijas
... 
... # Graficar el patrón de interferencia
... plt.figure(figsize=(10, 5))
... plt.plot(x, I, color='blue')
... plt.title("Simulación del Experimento de la Doble Rendija")
... plt.xlabel("Posición en la pantalla (m)")
... plt.ylabel("Intensidad (I)")
... plt.grid(True)
... 
... # Mostrar la gráfica
