import pandas as pd
import plotly.express as px
import streamlit as st

# Especifica la ruta completa del archivo CSV
file_path = 'vehicles_us.csv'

# Lee el archivo CSV y lo guarda en un DataFrame de pandas
vehicles_df = pd.read_csv(file_path)

# Muestra las primeras filas del DataFrame para verificar que se ha leído correctamente
st.write(vehicles_df.head())  

st.write("¡Bienvenido a mi aplicación Streamlit para visualización de datos!")
st.write("Aquí puedes explorar diferentes visualizaciones de datos sobre vehículos en venta en Estados Unidos.")

# Función para construir histograma
def build_histogram():
    st.write('Construyendo un histograma para la columna odómetro')
    fig = px.histogram(vehicles_df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Función para construir gráfico de dispersión
def build_scatter():
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(vehicles_df, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Botones para construir gráficos
if st.button('Construir histograma'):
    build_histogram()

if st.button('Construir gráfico de dispersión'):
    build_scatter()

st.write("Espero que disfrutes explorando los datos. ¡Diviértete!")
