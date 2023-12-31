# ---------------------------------------------------------- CARGA DE LIBRERÍAS
import os
import sys
import pandas as pd
import streamlit as st

from io import StringIO

# Ruta absoluta de directorio actual
DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# Ruta absoluta del directorio de módulos
SRC_PATH = os.path.join(DIR_PATH, '..', 'src')

# Agregar ruta de módulo al path
sys.path.append(SRC_PATH)

from ajustes import guardar_archivo
from ajustes import Ajustes


# ----------------------------------------------------------- AJUSTES GENERALES

# Carga de ajustes generales
ajustes = Ajustes()

# Site settings
st.set_page_config(
    page_title = ajustes.config['app']['paginas'][1]
    ,layout = 'wide'
    ,initial_sidebar_state = 'expanded')

# Título de la pagina
st.title(body = 'Consultas')
st.write('---')

# -------------------------------------------- LECTURA DE CRITERIOS DE BÚSQUEDA
CRITERIOS = os.path.join(
    ajustes.ROOT
    ,ajustes.config['datos']['dirname']
    ,ajustes.config['datos']['criterios']['dirname']
    ,ajustes.config['datos']['criterios']['workfile'])

try:
    # Abrir archivo de criterios de búsqueda
    with open(file = CRITERIOS, mode='r') as file:
        __criterios__ = file.read().splitlines()
    file.close()

# Excepción de archivo de criterios de búsqueda inexistente
except FileNotFoundError:
    __criterios__ = None

    st.write(f'''
        <br>No existe el archivo
        <b>{ajustes.config['datos']['criterios']['workfile']}</b>
        en la ruta: <b>{CRITERIOS}</b></br>
        <br>Utiliza la barra lateral para cargar un archivo de criterios de
        búsqueda.</br>'''
        ,unsafe_allow_html=True)
   

# --------------------------------------------------------------- BARRA LATERAL

# Ancho de barra lateral
ajustes.fijar_ancho_barra_lateral()

with st.sidebar:

    # Descripción de la barra lateral
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
        label = 'Cargar archivo:'
        ,type = 'txt'
        ,accept_multiple_files = False
        ,help = '''Carga aquí tu archivo de criterios de búsqueda cuando
        existan modificaciones a la información desplegada actualmente''')

    # ----------------------------------------------- CARGA DE NUEVOS CRITERIOS

    # Acciones si existe nuevo archivo de criterios de búsqueda
    if nuevos_criterios_busqueda is not None:
        
        # Leer archivo cargado como cadena de caracteres
        __archivo__ = StringIO(
            initial_value = (
                nuevos_criterios_busqueda
                .getvalue()
                .decode("utf-8")
                ))
        
        # Generar lista de nuevos criterios
        __criterios__ = [
            linea.strip()
            for linea in __archivo__.read().splitlines()
            if linea.strip()]
        
        # Vista previa de nuevos criterios como cadena de caracteres
        vista_previa = ', '.join(__criterios__[:2])
        vista_previa += ', ..., ' + ', '.join(__criterios__[-2:])

        st.write('Se detectaron los siguientes criterios:')
        st.write(f'''<b>{vista_previa}</b>''', unsafe_allow_html = True)

        # Mensaje de confirmación
        st.write('''
            <p style="text-align: justify">
                Al seleccionar esta opción, el archivo que cargaste
                será el nuevo documento de referencia, haciendo que los cambios
                en la aplicación sean permamentes</p>'''
            ,unsafe_allow_html=True)
        
        # Botón de confirmación
        st.button(
            label = 'Entiendo, guardar cambios'
            ,type = 'primary'
            ,on_click = guardar_archivo
            ,kwargs = {
                'contenido': __criterios__
                ,'path': CRITERIOS
                ,'formato': 'txt'}
            ,use_container_width = True)

if __criterios__ != None:
    
    # Ordenar lista de criterios de búsqeuda
    __criterios__.sort()


# --------------------------------------------------------- RESUMEN DE CONSULTA
    with st.container():
        # Encabezado de sección
        st.header(
            body = 'Resumen de consultas')

        # Descripción de sección
        st.write(
            '''
            <p style="text-align: justify">
            La siguiente tabla es un resumen de las consultas realizadas
            para cada uno de los criterios enlistados en el archivo
            <b>criterios_busqueda.txt</b>. En las filas se encuentran
            los criterios de búsqueda, mientras que en las columnas
            se indica el tipo de consulta en cuestión. Los criterios se
            pueden encontrar en 2 estados:
            <ul>
                <li>Verdadero: Se cuenta con información de ese criterio
                del tipo de consulta en cuestión</li>
                <li>Falso: No se cuente con información de ese criterio para
                la consulta dada</li>
            </ul>
            </p>'''
            ,unsafe_allow_html = True)
        
        df_ = pd.DataFrame(
            data = {
                'Interes Tiempo': False
                ,'Interes Region': False
                ,'Temas Relacionados': False}
            ,index = __criterios__)
        
        st.dataframe(
            data = df_
            ,use_container_width = True)
