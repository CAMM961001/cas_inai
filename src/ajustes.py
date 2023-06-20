import os
import yaml
import shutil

from streamlit import write
from datetime import datetime


def guardar_archivo(contenido:str, path:str, formato = 'txt'):
    """
    Esta función es para almacenar el contenido de un archivo
    en una ruta dada, generando a su vez un respaldo de archivos previos con
    el mismo nombre en caso de existir en un directorio de históricos.

    Parámetros:
    - contenido: Contenido del archivo que se almacenará
    - path: Ruta en la que se almacenará
    - formato: Extensión del archivo
    """

    # Extraer directorio del archivo
    dir = os.path.dirname(path)

    # Extraer nombre original del archivo
    filename = os.path.basename(path)

    # Respaldar archivo anterior si existe
    if os.path.isfile(path = path):

        # Agregar sufijo de fecha de respaldo
        newname = filename.partition(f'.{formato}')[0]
        newname += f"_{datetime.now().strftime('%Y%m%d-%H%M%S')}.{formato}"

        # Archivo de destino
        dst = os.path.join(dir, 'historico', newname)
        
        # Mover archivo a carpeta de históricos
        shutil.move(src=path, dst=dst)

        # Mensaje de confirmación
        write(
            f'Se respaldó versión previa con el nombre: <b>{newname}</b>'
            ,unsafe_allow_html = True)
    
    # Escribir nuevo archivo
    with open(file = path, mode = 'w') as file:
        file.write('\n'.join(contenido))
    file.close()

    # Mensaje de confirmación
    write(
        f'Nuevo archivo almacenado en la ruta: <br><b>{path}</b>'
        ,unsafe_allow_html = True)


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
