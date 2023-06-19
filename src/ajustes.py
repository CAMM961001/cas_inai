import os
import yaml
import shutil

from streamlit import write
from datetime import datetime


def guardar_archivo(path:str):
    # Respaldar archivo anterior si existe
    if os.path.isfile(path = path):
        # Extraer nombre original del archivo
        dst = path.partition('.txt')[0]
        
        # Agregar sufijo de fecha de respaldo
        dst += f"_{datetime.now().strftime('%Y%m%d%-H%M%S')}.txt"
        
        # Mover archivo de carpeta de históricos
        shutil.move(src=path, dst=dst)

    prompt = f'Archivo almacenado en la ruta: <br><b>{path}</b>'
    write(prompt, unsafe_allow_html = True)


class Ajustes:


    def __init__(self):
        """Initialize the app's static settings"""
        # Relative path to directory root
        self.ROOT = os.path.dirname(os.path.dirname(__file__))
        
        # Open global configuration file
        with open(os.path.join(self.ROOT, 'config.yml'), 'r') as file:
            self.config = yaml.safe_load(file)
        file.close


    def fijar_ancho_barra_lateral(self):
        # HTML para barra lateral de ancho fijo
        _html_str_ = '''
        <style>
            [data-testid="stSidebar"][aria-expanded="true"]{
                min-width: 325px;
                max-width: 325px;
            }'''

        # Indicar a streamlit ancho fijo
        write(
            _html_str_
            ,unsafe_allow_html = True)
