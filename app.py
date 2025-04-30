# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración básica de la página
st.set_page_config(page_title="Análisis de Vehículos", page_icon="🚗")

# Título de la aplicación
st.title("📊 Análisis Exploratorio de Datos de Vehículos")
st.markdown("---")

# Cargar los datos
@st.cache_data  # Esto cachea los datos para mejor performance
def load_data():
    return pd.read_csv('vehicles_us.csv')  # Asegúrate de que la ruta al archivo es correcta

df = load_data()

# Mostrar el dataframe (opcional)
st.header("🔍 Vista previa de los datos")
if st.checkbox("Mostrar datos crudos"):
    st.write(df)

# Sección de histograma interactivo
st.header("📈 Histograma Interactivo")
st.write("Selecciona una variable para visualizar su distribución:")

# Seleccionar columna para el histograma
column = st.selectbox(
    "Elige una columna:",
    options=df.select_dtypes(include=['float64', 'int64']).columns,
    index=0
)

# Crear y mostrar histograma cuando se hace clic en el botón
if st.button("Generar Histograma"):
    st.write(f"Histograma de {column}")
    
    fig = px.histogram(
        df, 
        x=column,
        title=f'Distribución de {column}',
        labels={column: column},
        color_discrete_sequence=['#1f77b4']
    )
    
    # Ajustes adicionales al gráfico
    fig.update_layout(
        bargap=0.1,
        xaxis_title=column,
        yaxis_title="Frecuencia"
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Sección de gráfico de dispersión
st.header("✨ Gráfico de Dispersión Interactivo")
st.write("Compara dos variables numéricas:")

col1, col2 = st.columns(2)

with col1:
    x_axis = st.selectbox(
        "Eje X:",
        options=df.select_dtypes(include=['float64', 'int64']).columns,
        index=0
    )

with col2:
    y_axis = st.selectbox(
        "Eje Y:",
        options=df.select_dtypes(include=['float64', 'int64']).columns,
        index=1
    )

if st.button("Generar Gráfico de Dispersión"):
    st.write(f"Relación entre {x_axis} y {y_axis}")
    
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        title=f'{x_axis} vs {y_axis}',
        color_discrete_sequence=['#ff7f0e'],
        hover_data=['model', 'type']
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Información adicional
st.markdown("---")
st.info("ℹ️ Esta aplicación permite explorar visualmente el dataset de vehículos usados.")
