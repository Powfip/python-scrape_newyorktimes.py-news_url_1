# Article Scraper

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)

## Descripción

**Article Scraper** es un script en Python que permite extraer el **título** y el **contenido** de artículos de páginas web de manera sencilla.  
Utiliza **Requests** para descargar la página y **BeautifulSoup** para parsear el HTML.  

Este proyecto es útil para aprender **web scraping básico**, extracción de contenido textual y manejo de HTML con Python.

---

## Funcionalidades

- Extrae el **título principal** (`<h1>`) de la página.  
- Extrae todos los párrafos (`<p>`) y los une en un texto continuo.  
- Manejo de errores si la URL no es proporcionada o no se encuentra el título.  
- Salida por consola, lista para almacenar o procesar posteriormente.

---

## Tecnologías y librerías

- Python 3.10+  
- Requests  
- BeautifulSoup (bs4)  

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/article_scraper.git
cd article_scraper
```

2. Crear un entorno virtual (opcional):

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

> Alternativamente, puedes instalar las librerías directamente:  

```bash
pip install requests beautifulsoup4
```

---

## Uso

Ejecuta el script proporcionando la URL del artículo como argumento:

```bash
python main.py "https://example.com/articulo"
```

Ejemplo de salida:

```
Título del artículo:
 Cómo aprender Python paso a paso

Contenido del artículo:
 Python es un lenguaje de programación...
 Se utiliza ampliamente en desarrollo web, ciencia de datos...
 ...
```

---

## Estructura del proyecto

```
article_scraper/
│
├── main.py          # Script principal con la función scrape_article()
├── requirements.txt
└── README.md
```

---

## Contribuciones

- Añadir soporte para múltiples artículos en lote.  
- Guardar resultados en CSV/JSON.  
- Añadir manejo de HTML más complejo (artículos con secciones o `<div>` específicos).  

---

## Licencia

MIT License. Consulta `LICENSE` para más información.

---

## Contacto

Para dudas o sugerencias: [123filipi@gmail.com]
