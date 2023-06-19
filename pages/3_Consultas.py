# ---------------------------------------------------------- CARGA DE LIBRERÍAS
import os
import sys
import streamlit as st

from io import StringIO

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
    page_title = ajustes.config['app']['paginas'][1]
    ,layout = 'wide'
    ,initial_sidebar_state = 'expanded')

# Título de la pagina
st.title(body = 'Consultas')


# --------------------------------------------------------------- BARRA LATERAL
ajustes.fijar_ancho_barra_lateral()

with st.sidebar:
    
    # Título de la página
    st.header(
        body = 'Acciones')

    # Descripción de la página
    st.write('''
        <p style="text-align: justify">
            <br>Utiliza las funciones de esta página para explorar los
            criterios de búsqueda de los cuales se tiene información.</br>
            <br>Utiliza la siguiente funcionalidad si deseas cargar un nuevo
            archivo de criterios de búsqueda.</br>
        </p>'''
        ,unsafe_allow_html = True)

    # Carga de archivo de criterios de búsqueda
    nuevos_criterios_busqueda = st.file_uploader(
        label = 'Carga de archivo de criterios de búsqueda:'
        ,type = 'txt'
        ,accept_multiple_files = False
        ,help = '''Carga aquí tu archivo de criterios de búsqueda cuando
        existan modificaciones a la información desplegada actualmente''')

    # ----------------------------------------------- CARGA DE NUEVOS CRITERIOS

    # Acciones si existe nuevo archivo de criterios de búsqueda
    if nuevos_criterios_busqueda is not None:
        
        # Leer archivo cargado como cadena de caracteres
        __archivo__ = StringIO(initial_value = (
            nuevos_criterios_busqueda
            .getvalue()
            .decode("utf-8")))
        
        # Generar lista de nuevos criterios
        __criterios__ = __archivo__.read().splitlines()

        # Respaldar archivo anterior


# -------------------------------------------- LECTURA DE CRITERIOS DE BÚSQUEDA
CRITERIOS = os.path.join(
    ajustes.ROOT
    ,ajustes.config['datos']['dirname']
    ,ajustes.config['datos']['criterios']['dirname']
    ,ajustes.config['datos']['criterios']['workfile'])

try:
    with open(file = CRITERIOS, mode='r') as file:
        CRITERIOS = file.read()
    file.close()

    print(CRITERIOS)

except FileNotFoundError:
    st.write(f'''
        <br>No existe el archivo
        <b>{ajustes.config['datos']['criterios']['workfile']}</b>
        en la ruta: <b>{CRITERIOS}</b></br>
        <br>Utiliza la barra lateral para cargar un archivo de criterios de
        búsqueda.</br>'''
        ,unsafe_allow_html=True)
