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
from folium.plugins import MarkerCluster

# -------------------- EXTRACCIÓN --------------------
df_2021 = pd.read_csv("datosAgs/Accidentes_ags_2021.csv", encoding='latin1')
df_2022 = pd.read_csv("datosAgs/Accidentes_ags_2022.csv", encoding='latin1')

df_2021['AÑO'] = 2021
df_2022['AÑO'] = 2022

# -------------------- TRANSFORMACIÓN --------------------
df_todos = pd.concat([df_2021, df_2022], ignore_index=True)

# Filtrar solo registros con coordenadas válidas
df_todos = df_todos.dropna(subset=['LATITUD', 'LONGITUD'])

# Opcional: Limitar número de registros por rendimiento (ej. 1000)
# df_todos = df_todos.sample(n=1000, random_state=42)

# -------------------- VISUALIZACIÓN: MAPA INTERACTIVO --------------------

# Crear mapa centrado en Aguascalientes
mapa = folium.Map(location=[21.8823, -102.2916], zoom_start=11, tiles='CartoDB positron')

# Agrupar marcadores
marcadores = MarkerCluster().add_to(mapa)

# Colores por año
colores = {2021: 'blue', 2022: 'red'}

# Añadir marcadores al mapa
for _, fila in df_todos.iterrows():
    folium.CircleMarker(
        location=[fila['LATITUD'], fila['LONGITUD']],
        radius=4,
        popup=(
            f"Año: {fila['AÑO']}<br>"
            f"Tipo: {fila['TIPACCID']}<br>"
            f"Muertos: {fila['TOTMUERTOS']}, Heridos: {fila['TOTHERIDOS']}"
        ),
        color=colores.get(fila['AÑO'], 'gray'),
        fill=True,
        fill_opacity=0.7
    ).add_to(marcadores)

# Guardar el mapa en archivo HTML
mapa.save("Mapa_Accidentes_Aguascalientes.html")
print("Mapa generado: Mapa_Accidentes_Aguascalientes.html")
