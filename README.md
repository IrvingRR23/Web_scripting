# WebScraper_Libros — Extracción de títulos con 4 y 5 estrellas

**Autor:** Irving Rodríguez Rodríguez  
**Lenguaje:** Python 3.7+  
**Estado:** Proyecto funcional y completado  

---

## Descripción general

Este proyecto realiza **web scraping** sobre el sitio [Books to Scrape](https://books.toscrape.com/) utilizando **BeautifulSoup** y **Requests**.  
El programa recorre automáticamente todas las páginas del catálogo, filtra los libros con **4 o 5 estrellas** y almacena la información en un archivo **CSV** con los siguientes datos:

- Título del libro  
- Calificación (rating)  
- Precio  

Además, el programa incluye manejo de errores, control de tiempo de ejecución y salida formateada en consola.

---

## Estructura del proyecto

| Archivo / Carpeta | Descripción | Función principal |
|--------------------|--------------|--------------------|
| `scraper_libros.py` | Código fuente principal | Realiza el scraping, filtra los libros y guarda los resultados |
| `libros_top.csv` | Archivo generado | Contiene los títulos, calificación y precio de los libros extraídos |

---

##  Dependencias

Este proyecto utiliza las siguientes librerías:

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
