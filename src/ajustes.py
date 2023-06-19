import os
import yaml

from streamlit import markdown


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
        markdown(
            body = _html_str_
            ,unsafe_allow_html = True)
