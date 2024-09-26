import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header('Cuadro de mandos de anuncios de coches')

# Crear botones para construir gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Si se hace clic en el botón de histograma
if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Si se hace clic en el botón de gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión: Precio vs. Odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Precio vs. Odómetro")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Opción adicional: usar casillas de verificación en lugar de botones
st.write("Opcional: Usa casillas de verificación para construir gráficos")

# Casillas de verificación
build_histogram = st.checkbox('Construir un histograma (opcional)')
build_scatter = st.checkbox('Construir un gráfico de dispersión (opcional)')

# Si la casilla de verificación de histograma está seleccionada
if build_histogram:
    st.write('Construyendo un histograma para la columna odómetro')
    fig_hist_opt = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist_opt, use_container_width=True)

# Si la casilla de verificación de dispersión está seleccionada
if build_scatter:
    st.write('Construyendo un gráfico de dispersión: Precio vs. Odómetro')
    fig_scatter_opt = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Precio vs. Odómetro")
    st.plotly_chart(fig_scatter_opt, use_container_width=True)
