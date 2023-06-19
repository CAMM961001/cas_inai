import streamlit as st

from src.ajustes import Ajustes


# ----------------------------------------------------------- AJUSTES GENERALES


ajustes = Ajustes()


# Site settings
st.set_page_config(
    page_title = ajustes.config['app']['titulo']
    ,layout = 'wide'
    ,initial_sidebar_state = 'expanded')


# --------------------------------------------------------------- BARRA LATERAL


ajustes.fijar_ancho_barra_lateral()

