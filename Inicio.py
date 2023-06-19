import streamlit as st

from streamlit_option_menu import option_menu

from src.ajustes import Ajustes


# ----------------------------------------------------------- AJUSTES GENERALES


ajustes = Ajustes()

# Site settings
st.set_page_config(
    page_title = ajustes.config['app']['titulo']
    ,layout = 'wide'
    ,initial_sidebar_state = 'expanded')


# --------------------------------------------------------------- BARRA LATERAL


# HTML para barra lateral de ancho fijo
_html_str_ = '''
<style>
    [data-testid="stSidebar"][aria-expanded="true"]{
        min-width: 325px;
        max-width: 325px;
    }'''

# Indicar a streamlit ancho fijo
st.markdown(
    body = _html_str_
    ,unsafe_allow_html = True)
