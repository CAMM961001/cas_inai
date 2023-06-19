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
    page_title = ajustes.config['app']['paginas'][1]
    ,layout = 'wide'
    ,initial_sidebar_state = 'expanded')


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

    # Acciones de la página
    archivo_criterio_busqueda = st.file_uploader(
        label = 'Carga de archivo de criterios de búsqueda:'
        ,type = 'txt'
        ,accept_multiple_files = False
        ,help = '''Carga aquí tu archivo de criterios de búsqueda cuando existan
        modificaciones a la información desplegada actualmente''')
    



# ----------------------------------------------------------- CARGA DE ARCHIVOS


if __name__ == '__main__':
    print(archivo_criterio_busqueda)
    print(type(archivo_criterio_busqueda))
