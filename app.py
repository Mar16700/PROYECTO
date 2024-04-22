import streamlit as st
import pandas as pd
import plotly_express as px

# Encabezado de la aplicación
st.header("Mi Aplicación Basada en Streamlit")

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Si se hace clic en el botón de histograma
if hist_button:
    # Mensaje informativo
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar el histograma
    st.plotly_chart(fig, use_container_width=True)

# Si se hace clic en el botón de gráfico de dispersión
if scatter_button:
    # Mensaje informativo
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y="price")
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)