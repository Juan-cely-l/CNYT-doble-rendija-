# CNYT-doble-rendija-
# 📊 Experimento de la Doble Rendija - Simulación en Python

Este repositorio implementa y simula el experimento clásico de la **doble rendija**, propuesto por Thomas Young en 1801 para demostrar la naturaleza ondulatoria de la luz. El experimento ilustra cómo la luz puede interferir consigo misma, generando patrones de interferencia que solo pueden explicarse si la luz se comporta como una onda.

## 📚 Explicación Teórica del Experimento

### ¿Qué es el Experimento de la Doble Rendija?
El experimento de la doble rendija consiste en dirigir un haz de luz coherente (como un láser) hacia un material opaco que tiene dos rendijas estrechas y paralelas. Cuando la luz atraviesa las dos rendijas, se difracta y las ondas emergentes interfieren entre sí, formando un patrón de franjas brillantes y oscuras en una pantalla ubicada detrás de las rendijas.

### ¿Por qué Ocurre la Interferencia?
Las ondas de luz provenientes de cada rendija se superponen. Esto significa que, dependiendo de la diferencia de fase entre las ondas (determinado por la distancia recorrida por cada onda desde su rendija hasta un punto en la pantalla), pueden interferir **constructivamente** (cuando las crestas de ambas ondas se suman, generando una franja brillante) o **destructivamente** (cuando una cresta y un valle se cancelan, formando una franja oscura).

El patrón de interferencia observado en la pantalla se puede describir usando la ecuación:

\[
d \cdot \sin \theta = m \cdot \lambda
\]

Donde:

- **d**: Distancia entre las rendijas.
- **θ**: Ángulo de interferencia para cada franja observada.
- **λ**: Longitud de onda de la luz utilizada.
- **m**: Número de orden (m = 0, ±1, ±2, ...).

Las franjas claras corresponden a los máximos de interferencia (m = ±1, ±2...) y las franjas oscuras a los mínimos de interferencia.

### Relevancia del Experimento
El experimento de la doble rendija es crucial en la física porque demuestra la **dualidad onda-partícula** de la luz y ha sido replicado incluso con partículas como electrones, mostrando que no solo las ondas de luz, sino también las partículas, exhiben propiedades ondulatorias bajo ciertas condiciones.



El propósito de este proyecto es simular este patrón de interferencia utilizando `numpy` para los cálculos y `matplotlib` para la visualización. El módulo permite visualizar cómo cambian las franjas de interferencia según se ajusten parámetros como la longitud de onda y la separación de las rendijas.

### 📋 Requisitos del Proyecto

- Python 3.x
- `numpy`
- `matplotlib`

fotos del experimento realizado :
![image](https://github.com/user-attachments/assets/a042c7ab-9eba-4fdb-a58a-b3c3ad1f0e5d)

![image](https://github.com/user-attachments/assets/a1d3378f-3757-4e48-a9f1-79b152b91caf)

### 📋 Patron de interferencia

![20240923_163755](https://github.com/user-attachments/assets/851fff3a-09df-4961-9e7d-9c6d2e877273)



  

