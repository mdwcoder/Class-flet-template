# Plantilla Flet con Estructura de Clase

Esta es una plantilla para proyectos Flet en Python. Está diseñada para funcionar como un único archivo (`main.py`) con una estructura basada en clases, lo cual permite organizar el código de manera más limpia y escalable, especialmente útil en aplicaciones de mayor complejidad.

## Descripción

En lugar de usar una función principal como punto de entrada para la aplicación, esta plantilla utiliza una clase `App`. Esto facilita la gestión de la interfaz y sus componentes, así como la configuración de la aplicación.

## Requisitos Previos

- **Python 3.9 o superior**.
- **Flet**: Instálalo usando:

  ```bash
  pip install flet
  
## Estructura de la Clase App
-  __init__: Inicializa la clase, configura la página, y agrega widgets iniciales.
-  config: Configura el título, color de fondo y alineación horizontal de la página.
-  add_widgets: Agrega los widgets a la página.

Esta plantilla proporciona un punto de partida limpio para organizar proyectos Flet más complejos con clases.

## Personalización

Puedes agregar widgets en la lista widgets y personalizar el método config para ajustar los atributos de la página según las necesidades de tu aplicación.
