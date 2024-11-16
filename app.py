import streamlit as st
import pandas as pd
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Clasificación de Prendas",
    page_icon="🧥",
    layout="wide",
)

# CSS para estilizar la aplicación
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f7f6;
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .header {
            text-align: center;
            font-size: 36px;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .upload-container {
            padding: 20px;
            border: 2px dashed #2ecc71;
            background-color: #eafaf1;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        .upload-container h3 {
            color: #2ecc71;
            font-size: 18px;
            margin-bottom: 10px;
        }
        .image-container, .features-container {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }
        .image-container {
            text-align: center;
        }
        .features-container {
            font-size: 16px;
            color: #34495e;
        }
        .features-container table {
            width: 100%;
            border-collapse: collapse;
        }
        .features-container th, .features-container td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .features-container th {
            background-color: #2980b9;
            color: white;
        }
        .description {
            margin-top: 20px;
            font-size: 14px;
            color: #7f8c8d;
        }
        .info-message {
            font-size: 18px;
            color: #2980b9;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título
st.markdown('<div class="header">🧥 Clasificación de Prendas</div>', unsafe_allow_html=True)
st.markdown("Sube una imagen de una prenda y obtén sus características detectadas por el modelo.")

# Carga de imagen
st.markdown('<div class="upload-container"><h3>📤 Subir Imagen</h3></div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

# División del layout en dos columnas
col1, col2 = st.columns([1, 2], gap="large")

if uploaded_file is not None:
    # Mostrar la imagen cargada en la primera columna
    with col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(Image.open(uploaded_file), caption="Imagen cargada", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Simulación de resultados del modelo y mostrarlos en la segunda columna
    with col2:
        st.markdown('<div class="features-container">', unsafe_allow_html=True)
        st.markdown("### Características detectadas:")
        
        # Simulación de datos de ejemplo
        simulated_data = {
            "Característica": ["Tipo de prenda", "Color", "Largo", "Corte", "Tamaño"],
            "Valor": ["Pantalón", "Azul", "Largo", "Regular", "Mediano"],
        }
        df = pd.DataFrame(simulated_data)
        st.table(df)
        
        st.markdown("### Descripción adicional:")
        st.write(
            """
            - **Tipo de prenda**: Pantalón, identificado por su estructura.
            - **Color**: Azul, basado en los píxeles dominantes.
            - **Largo**: Largo, por la proporción de la prenda.
            - **Corte**: Regular, no es ajustado ni oversized.
            - **Tamaño**: Mediano, estimado visualmente.
            """
        )
        st.markdown('</div>', unsafe_allow_html=True)
else:
    with col1:
        st.markdown('<div class="info-message">Esperando imagen para mostrar resultados.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="info-message">Por favor sube una imagen de la prenda.</div>', unsafe_allow_html=True)
