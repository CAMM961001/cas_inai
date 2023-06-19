# ---------------------------------------------------------- CARGA DE LIBRERÍAS


import os
import sys
import streamlit as st

# Ruta absoluta de directorio actual
DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# Ruta absoluta del directorio de módulos
SRC_PATH = os.path.join(DIR_PATH, '..', 'src')

# Agregar ruta de módulo al path
sys.path.append(SRC_PATH)

from ajustes import Ajustes


# ----------------------------------------------------------- AJUSTES GENERALES


ajustes = Ajustes()


# Site settings
st.set_page_config(
    page_title = ajustes.config['app']['paginas'][0]
    ,layout = 'wide'
    ,initial_sidebar_state = 'expanded')


# --------------------------------------------------------------- BARRA LATERAL


ajustes.fijar_ancho_barra_lateral()

with st.sidebar:
    st.title('Visualizaciones')
