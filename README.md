# Contenido

- [Descripción del problema](#descripción-del-problema)
    - [Glosario de términos](#glosario-de-términos)
- [Pytrends](#pytrends)
    - [Métodos de API](#métodos-de-api)
- [Arquitectura general](#arquitectura-general)
- [Entorno virtual](#entorno-virtual)

# Descripción del problema

Proyecto de adquisición y monitoreo de datos de Google Trends para el Centro de Atención a la Sociedad del Instituto Nacional de Acceso a la Información y Protección de Datos Personales, INAI. Se definireron los siguientes requisitos que deben satisfacer las consultas a la API:

-   Hacer consultas histróricas utilizando palabras clave.
-   Tener capacidad de hacer consultas bajo demanda.
-   Basado en tecnología abierta.

Para satisfacer los puntos anteriores, se determinó utilizar la API de Python para consultar información de GoogleTrends.

## Glosario de términos

- Criterio de búsqueda: Palabra o serie de palabras que usualmente se buscarían en un motor como Google o Firefox. 

# Pytrends

Los métodos de `pytrends` típicamente utilizan los siguientes parámetros:
-   `kw_list`: Lista de pálabras clave o criterios de búsqueda
-   `cat`: Categoría para reducir resultados
-   `geo`: Abrebiación de dos letras de un país (`MX` para México)
-   `tz`: Offset de zona horaria en minutos, para más información ir a la [liga](https://en.wikipedia.org/wiki/UTC_offset) (México es _UTC-6_ lo cual resulta en un offset de `360`)
-   `timeframe`: Ventana de tiempo de consulta
-   `gprop`: (Metadato) Propiedad de google que se quiere filtrar

En el siguiente [enlace](https://pypi.org/project/pytrends/) se puede encontrar la documentación oficial de la API.

## Métodos de API

Para satisfacer propósitos del proyecto, se realizarán consultas a la API a través de los siguientes métodos:

`pytrends.interest_over_time()`

>Regresa datos históricos indexados para los momentos en los que los criterios de búsqueda, definidos en `kw_list`, tuvieron una mayor cantidad de búsquedas.
>
>**IMPORTANTE**: Los números representan el interés de búsqueda en relación con el valor máximo de la lista correspondiente a la región y el período especificados. El valor 100 indica la popularidad máxima del término, 50 implica la mitad de popularidad, y 0 significa que no hubo suficientes datos para este término

`pytrends.interest_by_region()`

>Regresa las regiones en las cuales la palabra fue más buscada.

`pytrends.related_topics()`

>Regresa un diccionario de dataframes que contienen información de las palabras clave relacionadas con el criterio de búsqueda. Esto lo hace en dos categorías:
>-  Temas top
>-  Temas en aumento

# Arquitectura general

![adquisicion-datos](/diagramas/arquitectura_general.drawio.png)

# Entorno virtual

Se utiliza un entorno virtual local debido a que este proyecto pertenece a un programa mucho más grande. Por este motivo, se utiliza el módulo para entornos virtuales de python `venv`. Para configurar el entorno de trabajo, se debe seguir los siguientes pasos:

1. Abrir una terminal.
2. Crear un entorno virtual con el comando `python -m venv <nombre-del-entorno>`

Windows Powershell:

>python -m venv venv

Linux Bash:

>python3 -m venv venv
