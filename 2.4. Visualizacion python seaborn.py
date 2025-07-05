# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  2.4 Ejercicios de Programación Avanzada con Python
# Objetivo: Programación, configuración y ejecución de instrucciones en Python
#           para aplicar la librería Seaborn en la graficación de 12 modelos
# Archivo fuente: [2.4. Visualizacion python_com.pdf]
# --------------------------------------------------------------------------

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import squarify

# Crear DataFrame simulado
data = pd.DataFrame({
    'Salary': [35000, 42000, 48000, 52000, 61000, 58000, 47000, 39000],
    'Age': [25, 28, 35, 40, 45, 38, 32, 27],
    'Education': ['Licenciatura', 'Maestría', 'Licenciatura', 'Doctorado', 'Maestría', 'Licenciatura', 'Maestría', 'Doctorado'],
    'Gender': ['F', 'M', 'M', 'F', 'F', 'M', 'F', 'M'],
    'District': ['Norte', 'Sur', 'Norte', 'Este', 'Oeste', 'Sur', 'Este', 'Norte'],
    'Groups': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'IQ score': [110, 125, 108, 130, 118, 105, 114, 120]
})

# 1. relplot
sns.set_style("ticks")
sns.relplot(x="Salary", y="Age", hue="Education", style="Education", col="Gender", data=data)
plt.show()

# 2. barplot
sns.set_style("whitegrid")
sns.barplot(x="Education", y="Salary", hue="District", data=data)
plt.title("Salario promedio por educación y distrito")
plt.show()

# 3. boxplot
sns.set_style('whitegrid')
sns.set_context("talk")
sns.boxplot(x='Groups', y='IQ score', data=data)
sns.despine(left=True, right=True, top=True)
plt.title('IQ scores for different test groups')
plt.show()

# 4. violinplot
sns.set_style("whitegrid")
sns.violinplot(x='Education', y='Salary', hue='Gender', data=data, split=True, cut=0)
plt.title('Distribución salarial por educación y género')
plt.show()

# 5. histplot + kdeplot
sns.histplot(data['Age'], kde=True)
plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Densidad")
plt.show()

# 6. jointplot
sns.set_style("white")
sns.jointplot(x="Salary", y="Age", data=data)
plt.show()

# 7. pairplot
sns.set_style("ticks")
sns.pairplot(data, hue='Education')
plt.show()

# 8. regplot
x = np.arange(100)
y = x + np.random.normal(0, 5, size=100)
sns.regplot(x=x, y=y)
plt.title("Relación lineal simulada")
plt.show()

# 9. heatmap (correlación)
sns.heatmap(data.corr(numeric_only=True), cmap="YlGnBu", annot=True)
plt.title("Mapa de calor de correlación")
plt.show()

# 10. FacetGrid
g = sns.FacetGrid(data, col="Gender", hue="Education")
g.map(plt.scatter, "Salary", "Age")
g.add_legend()
plt.show()

# 11. treemap con squarify
colors = sns.light_palette("brown", 4)
squarify.plot(sizes=[50, 25, 10, 15], label=["A", "B", "C", "D"], color=colors)
plt.axis("off")
plt.title("Distribución de grupos")
plt.show()

