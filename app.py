import pandas as pd
import plotly.express as px
import streamlit as st


# Especifica la ruta completa del archivo CSV
file_path = 'vehicles_us.csv'

# Lee el archivo CSV y lo guarda en un DataFrame de pandas
vehicles_df = pd.read_csv(file_path)

# Muestra las primeras filas del DataFrame para verificar que se ha leído correctamente
st.write(vehicles_df.head())  # Usamos st.write en lugar de print para mostrar las filas en Streamlit

st.write("¡Bienvenido a mi aplicación Streamlit para visualización de datos!")
st.write("Aquí puedes explorar diferentes visualizaciones de datos sobre vehículos en venta en Estados Unidos.")

# Código para construir un histograma interactivo
# Utiliza un botón para permitir al usuario generar el histograma

# Crear un encabezado
st.header('Análisis de Datos de Vehículos Usados en EE.UU.')

# Crear un botón
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(vehicles_df, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Código para construir un gráfico de dispersión interactivo
# Utiliza un botón para permitir al usuario generar el gráfico de dispersión

# Lee los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="year", y="price", color="manufacturer")
    st.plotly_chart(fig, use_container_width=True)


# Código para construir un histograma y un gráfico de dispersión interactivos
# Utiliza casillas de verificación para permitir al usuario elegir qué gráfico mostrar

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')

# Construir el histograma si la casilla de verificación está seleccionada
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Construir el diagrama de dispersión si la casilla de verificación está seleccionada
if build_scatter:
    st.write('Construir un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="year", y="price", color="manufacturer")
    st.plotly_chart(fig, use_container_width=True)

st.write("Espero que disfrutes explorando los datos. ¡Diviértete!")
