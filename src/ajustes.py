import os
import yaml

from streamlit import write


def guardar_archivo(path:str):
    promtp = f'Archivo almacenado en la ruta: <br><b>{path}</b>'
    write(promtp, unsafe_allow_html = True)


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
