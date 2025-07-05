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
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de gráficos
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# -------------------- EXTRACCIÓN DE DATOS --------------------
# Ajusta las rutas si lo ejecutas localmente
df_2021 = pd.read_csv("datosAgs/Accidentes_ags_2021.csv", encoding='latin1')
df_2022 = pd.read_csv("datosAgs/Accidentes_ags_2022.csv", encoding='latin1')

# -------------------- TRANSFORMACIÓN DE DATOS --------------------
# Agregamos el año para diferenciar los conjuntos
df_2021["AÑO"] = 2021
df_2022["AÑO"] = 2022

# Unificamos ambos años en un solo DataFrame
df_todos = pd.concat([df_2021, df_2022], ignore_index=True)

# Limpiamos columnas clave
df_todos['TIPACCID'] = df_todos['TIPACCID'].fillna("NO ESPECIFICADO")
df_todos['HORA'] = pd.to_numeric(df_todos['HORA'], errors='coerce').fillna(-1).astype(int)
df_todos['MES'] = pd.to_numeric(df_todos['MES'], errors='coerce').fillna(0).astype(int)

# Convertimos valores de día de la semana
dias_semana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
df_todos['DIASEMANA_NOMBRE'] = df_todos['DIASEMANA'].apply(lambda x: dias_semana[x - 1] if 1 <= x <= 7 else 'Desconocido')

# -------------------- GRÁFICA 5: MAPA DE CALOR DE UBICACIÓN --------------------
plt.figure()
sns.kdeplot(
    data=df_todos.dropna(subset=['LATITUD', 'LONGITUD']),
    x="LONGITUD", y="LATITUD", fill=True, cmap="Reds", bw_adjust=0.5
)
plt.title('Mapa de calor de ubicación de accidentes (2021-2022)')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.tight_layout()
plt.show()

# -------------------- GRÁFICA 6: ACCIDENTES POR DÍA DE LA SEMANA --------------------
acc_dia_semana = df_todos.groupby(['AÑO', 'DIASEMANA_NOMBRE']).size().reset_index(name='Total')
acc_dia_semana['DIASEMANA_NOMBRE'] = pd.Categorical(acc_dia_semana['DIASEMANA_NOMBRE'], categories=dias_semana, ordered=True)
acc_dia_semana = acc_dia_semana.sort_values(['AÑO', 'DIASEMANA_NOMBRE'])

plt.figure()
sns.barplot(data=acc_dia_semana, x='DIASEMANA_NOMBRE', y='Total', hue='AÑO')
plt.title('Accidentes por día de la semana (2021 vs 2022)')
plt.xlabel('Día de la semana')
plt.ylabel('Número de accidentes')
plt.legend(title='Año')
plt.tight_layout()
plt.show()

# -------------------- GRÁFICA 7: ACCIDENTES POR ZONA URBANA VS SUBURBANA --------------------
zona_urbana = df_todos.groupby('AÑO')['URBANA'].sum()
zona_suburbana = df_todos.groupby('AÑO')['SUBURBANA'].sum()

zona_comparativa = pd.DataFrame({
    'AÑO': [2021, 2021, 2022, 2022],
    'ZONA': ['Urbana', 'Suburbana'] * 2,
    'TOTAL': [zona_urbana[2021], zona_suburbana[2021], zona_urbana[2022], zona_suburbana[2022]]
})

plt.figure()
sns.barplot(data=zona_comparativa, x='ZONA', y='TOTAL', hue='AÑO')
plt.title('Accidentes por zona: Urbana vs Suburbana')
plt.xlabel('Zona')
plt.ylabel('Número de accidentes')
plt.legend(title='Año')
plt.tight_layout()
plt.show()
