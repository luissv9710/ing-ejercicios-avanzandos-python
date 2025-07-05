# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  Análisis de datos masivos de una caso real, para su graficación y conclusión
# Objetivo: Analizar un caso real con información origen de CSVs de dos años
#           consecutivos sobre accidentes en Aguascalientes, para generar
#           gráficas representativas y generar conclusiones y recomendaciones válidas
# Archivo fuente: [2.5. Actividad_U2_python.pdf]
# NOTA:     Se dividió en dos programas debido a los tipos de gráficas generadas
#           Esta a la parte 2
# --------------------------------------------------------------------------


# -------------------- IMPORTACIÓN DE LIBRERÍAS --------------------
import pandas as pd
import folium
from folium.plugins import HeatMap

# -------------------- EXTRACCIÓN Y TRANSFORMACIÓN --------------------
# Cargar datos
df_2021 = pd.read_csv("datosAgs/Accidentes_ags_2021.csv", encoding='latin1')
df_2022 = pd.read_csv("datosAgs/Accidentes_ags_2022.csv", encoding='latin1')

# Añadir columna de año
df_2021['AÑO'] = 2021
df_2022['AÑO'] = 2022

# Unir ambos DataFrames
df_todos = pd.concat([df_2021, df_2022], ignore_index=True)

# Filtrar coordenadas válidas
df_mapa = df_todos.dropna(subset=['LATITUD', 'LONGITUD'])

# -------------------- CREACIÓN DE HEATMAP --------------------

# Crear mapa base centrado en Aguascalientes
#mapa_heat = folium.Map(location=[21.8823, -102.2916], zoom_start=11, tiles='Stamen Toner')
mapa_heat = folium.Map(location=[21.8823, -102.2916], zoom_start=11, tiles='CartoDB positron')


# Crear lista de coordenadas
coordenadas = df_mapa[['LATITUD', 'LONGITUD']].values.tolist()

# Agregar HeatMap al mapa
HeatMap(data=coordenadas, radius=10, blur=15, max_zoom=13).add_to(mapa_heat)

# Guardar el mapa interactivo
mapa_heat.save("Heatmap_Concentracion_Accidentes.html")
print("Mapa generado: Heatmap_Concentracion_Accidentes.html")

