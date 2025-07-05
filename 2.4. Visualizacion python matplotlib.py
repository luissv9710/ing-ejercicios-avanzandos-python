# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  2.4 Ejercicios de Programación Avanzada con Python
# Objetivo: Programación, configuración y ejecución de instrucciones en Python
#           para aplicar la librería Matplotlib en la graficación de 12 modelos
# Archivo fuente: [2.4. Visualizacion python_com.pdf]
# --------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

# 1. Gráfico de línea
plt.plot([1, 2, 4, 5], [1, 3, 4, 3], '-o')
plt.title('Tendencia de valores')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.show()

# 2. Barras verticales
plt.bar(['A', 'B', 'C'], [10, 20, 15])
plt.title('Ventas por producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.show()

# 3. Barras horizontales
plt.barh(['Producto A', 'Producto B', 'Producto C', 'Producto D'], [100, 150, 130, 160])
plt.title('Ingresos por producto')
plt.xlabel('Ingresos')
plt.ylabel('Producto')
plt.show()

# 4. Gráfico de pastel
plt.pie([40, 35, 25], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title('Distribución de mercado')
plt.show()

# 5. Histograma de distribución
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Distribución de frecuencias')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

# 6. Boxplot
data = [7, 15, 14, 10, 10, 12, 20]
plt.boxplot(data)
plt.title('Distribución de datos')
plt.ylabel('Valores')
plt.show()

# 7. Gráfico de dispersión (scatter)
x = [5, 7, 8, 7, 2, 17, 2, 9, 6, 10, 7, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87, 79, 110, 87, 96]
plt.scatter(x, y)
plt.title('Relación entre X e Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# 8. Gráfico de burbujas
x = [10, 20, 30, 15, 25, 35, 40]
y = [100, 200, 300, 150, 100, 200, 145]
z = [15, 25, 35, 45, 55, 65, 75]
plt.scatter(x, y, s=[i * 10 for i in z], alpha=0.5)
plt.title('Gráfico de burbujas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# 9. Gráfico de radar
labels = ['Eficiencia', 'Calidad', 'Compromiso', 'Responsabilidad', 'Cooperación']
values = [8, 9, 6, 7, 8]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, 'o-', linewidth=2)
ax.fill(angles, values, alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
plt.title('Desempeño del empleado')
plt.show()

# 10. Barras apiladas
days = ['Lun', 'Mar', 'Mié']
smokers = [10, 12, 14]
non_smokers = [20, 22, 24]
plt.bar(days, smokers, label='Fumadores')
plt.bar(days, non_smokers, bottom=smokers, label='No fumadores')
plt.title('Ventas por día y tipo de cliente')
plt.ylabel('Ventas')
plt.legend()
plt.show()

# 11. Área apilada
x = [1, 2, 3, 4]
y1 = [2, 4, 5, 8]
y2 = [1, 5, 4, 2]
plt.stackplot(x, y1, y2, labels=['Serie A', 'Serie B'])
plt.title('Áreas apiladas')
plt.xlabel('Periodo')
plt.ylabel('Valor')
plt.legend()
plt.show()

# 12. Histograma 2D
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.hist2d(x, y, bins=30)
plt.title('Histograma 2D')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()
