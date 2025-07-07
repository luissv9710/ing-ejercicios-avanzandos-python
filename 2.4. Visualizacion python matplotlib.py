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
import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.read_csv("smartphone_sales.csv")

# 1. Gráfico de línea
plt.figure(figsize=(10,5))
plt.plot(df_sales['Quarter'], df_sales['Apple'], '-o', label='Apple', color='green')
plt.title('Tendencia de Ventas de Apple por Trimestre')
plt.xlabel('Trimestre')
plt.ylabel('Ventas (en miles de unidades)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Barras verticales
trimestre_especifico = df_sales[df_sales['Quarter'] == '4Q16'].iloc[0]
marcas = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO']
ventas = [trimestre_especifico[m] for m in marcas]

# Gráfica de barras verticales
plt.figure(figsize=(8,5))
plt.bar(marcas, ventas, color='steelblue')
plt.title('Ventas por Marca - Trimestre 4Q16')
plt.xlabel('Marca')
plt.ylabel('Ventas (en miles de unidades)')
plt.tight_layout()
plt.show()




# 3. Barras horizontales
# Promedio de ventas por marca
promedios = df_sales[marcas].mean()

# Gráfica de barras horizontales
plt.figure(figsize=(8,5))
plt.barh(marcas, promedios, color='darkorange')
plt.title('Promedio de Ventas por Marca')
plt.xlabel('Ventas promedio por trimestre')
plt.ylabel('Marca')
plt.tight_layout()
plt.show()



# 4. Gráfico de pastel
plt.pie([15, 28, 32, 8, 17], labels=['Apple', 'Huawei', 'Samsung', 'Oppo', 'Xiaomi'], autopct='%1.1f%%')
plt.title('Distribución de marcas')
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
plt.title('Distribución de ventas (smarphones)')
plt.ylabel('Valores')
plt.show()

# 7. Gráfico de dispersión (scatter)
x = [5, 7, 8, 7, 2, 17, 2, 9, 6, 10, 7, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87, 79, 110, 87, 96]
plt.scatter(x, y)
plt.title('Relación entre smartphone y ventas')
plt.xlabel('Smartphone')
plt.ylabel('Ventas')
plt.show()

# 8. Gráfico de burbujas
x = [10, 20, 30, 15, 25, 35, 40]
y = [100, 200, 300, 150, 100, 200, 145]
z = [15, 25, 35, 45, 55, 65, 75]
plt.scatter(x, y, s=[i * 10 for i in z], alpha=0.5)
plt.title('Gráfico de burbujas')
plt.xlabel('Smartphone')
plt.ylabel('Ventas')
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
days = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie']
clients = [10, 12, 14, 25, 18]
non_clients = [20, 22, 24, 26, 50]
plt.bar(days, clients, label='Clientes')
plt.bar(days, non_clients, bottom=clients, label='Prospectos')
plt.title('Ventas por día y tipo de cliente')
plt.ylabel('Ventas')
plt.legend()
plt.show()

# 11. Área apilada
x = [1, 2, 3, 4]
y1 = [2, 4, 5, 8]
y2 = [1, 5, 4, 2]
plt.stackplot(x, y1, y2, labels=['Serie A', 'Serie B'])
plt.title('Áreas ventas')
plt.xlabel('Smartphone')
plt.ylabel('Ventas')
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
