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
#           Esta a la parte 1
# --------------------------------------------------------------------------

# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo para las gráficas
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# -------------------- ETAPA 1: EXTRACCIÓN --------------------
# Cargar archivos CSV desde ruta local
ruta_2021 = "datosAgs/Accidentes_ags_2021.csv"
ruta_2022 = "datosAgs/Accidentes_ags_2022.csv"

# Usamos encoding 'latin1' por caracteres especiales
df_2021 = pd.read_csv(ruta_2021, encoding='latin1')
df_2022 = pd.read_csv(ruta_2022, encoding='latin1')

# -------------------- ETAPA 2: TRANSFORMACIÓN --------------------
# Añadir columna 'AÑO' para diferenciar registros
df_2021['AÑO'] = 2021
df_2022['AÑO'] = 2022

# Unificar ambos DataFrames
df_todos = pd.concat([df_2021, df_2022], ignore_index=True)

# Limpiar valores faltantes en columnas clave
df_todos['TIPACCID'] = df_todos['TIPACCID'].fillna("NO ESPECIFICADO")
df_todos['HORA'] = pd.to_numeric(df_todos['HORA'], errors='coerce').fillna(-1).astype(int)
df_todos['MES'] = pd.to_numeric(df_todos['MES'], errors='coerce').fillna(0).astype(int)

# Agrupar por nombre de mes
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df_todos['MES_NOMBRE'] = df_todos['MES'].apply(lambda x: meses[x-1] if 1 <= x <= 12 else 'Desconocido')

# -------------------- ETAPA 3: CARGA PARA VISUALIZACIÓN --------------------

# -------------------- GRÁFICA 1: Tendencia mensual --------------------
tendencia_mensual = df_todos.groupby(['AÑO', 'MES_NOMBRE']).size().reset_index(name='TOTAL')
# Asegurar orden de los meses
tendencia_mensual['MES_NOMBRE'] = pd.Categorical(tendencia_mensual['MES_NOMBRE'], categories=meses, ordered=True)
tendencia_mensual = tendencia_mensual.sort_values(['AÑO', 'MES_NOMBRE'])

plt.figure()
sns.lineplot(data=tendencia_mensual, x='MES_NOMBRE', y='TOTAL', hue='AÑO', marker='o')
plt.title('Comparación mensual de accidentes viales (2021 vs 2022)')
plt.xlabel('Mes')
plt.ylabel('Número de accidentes')
plt.legend(title='Año')
plt.tight_layout()
plt.show()

# -------------------- GRÁFICA 2: Total de fallecidos y heridos por año --------------------
victimas = df_todos.groupby('AÑO')[['TOTMUERTOS', 'TOTHERIDOS']].sum().reset_index()

plt.figure(figsize=(8,5))
bar1 = plt.bar(victimas['AÑO'] - 0.2, victimas['TOTHERIDOS'], width=0.4, label='Heridos', color='orange')
bar2 = plt.bar(victimas['AÑO'] + 0.2, victimas['TOTMUERTOS'], width=0.4, label='Fallecidos', color='crimson')

# Etiquetas de valor con color correspondiente
for i in range(len(victimas)):
    plt.text(victimas['AÑO'][i] - 0.2, victimas['TOTHERIDOS'][i] + 10, str(victimas['TOTHERIDOS'][i]),
             ha='center', fontsize=10, color='orange')
    plt.text(victimas['AÑO'][i] + 0.2, victimas['TOTMUERTOS'][i] + 5, str(victimas['TOTMUERTOS'][i]),
             ha='center', fontsize=10, color='crimson')

plt.title("Total de Víctimas por Año (Heridos y Fallecidos)")
plt.ylabel("Número de personas")
plt.xticks(victimas['AÑO'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# -------------------- GRÁFICA 3: Distribución por tipo de accidente --------------------
# Diccionario de descripciones de tipos de accidente
descripcion_tipaccid = {
    0: "Certificado cero",
    1: "Colisión con vehículo automotor",
    2: "Atropellamiento",
    3: "Colisión con animal",
    4: "Colisión con objeto fijo",
    5: "Volcadura",
    6: "Caída de pasajero",
    7: "Salida del camino",
    8: "Incendio",
    9: "Colisión con ferrocarril",
    10: "Colisión con motocicleta",
    11: "Colisión con ciclista",
    12: "Otro"
}

# Contar tipo de accidente por año
tipos = df_todos.groupby(['AÑO', 'TIPACCID']).size().reset_index(name='CUENTA')
tipos['TIPO_DESC'] = tipos['TIPACCID'].map(descripcion_tipaccid)

# Gráfico
plt.figure(figsize=(10,6))
sns.barplot(data=tipos, x='CUENTA', y='TIPO_DESC', hue='AÑO')
plt.title("Distribución de Accidentes por Tipo y Año")
plt.xlabel("Cantidad de accidentes")
plt.ylabel("Tipo de accidente")
plt.legend(title="Año")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# -------------------- GRÁFICA 4: Accidentes por hora del día --------------------
acc_por_hora = df_todos[df_todos['HORA'] >= 0].groupby(['AÑO', 'HORA']).size().reset_index(name='Total')

plt.figure()
sns.lineplot(data=acc_por_hora, x='HORA', y='Total', hue='AÑO', marker='o')
plt.title('Accidentes viales por hora del día (2021 vs 2022)')
plt.xlabel('Hora del día')
plt.ylabel('Cantidad de accidentes')
plt.xticks(range(0, 24))
plt.legend(title='Año')
plt.tight_layout()
plt.show()
