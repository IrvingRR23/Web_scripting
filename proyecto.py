import bs4
import requests
import csv
import time

#Crear una url sin numero de pagina
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

#lista de titulos con mas de 4 estrellas
titulos_top = []

#Se inicia el temporizador
inicio = time.time()

print("\n Iniciando recopilacion de datos... \n")

# Recorre las 50 páginas del catálogo
for pagina in range (1,51):
    try:
        url_pagina = url_base.format(pagina)
        resultado = requests.get(url_pagina, timeout=5)
        resultado.raise_for_status()
    except Exception as e:
        print(f"Error en la página {pagina}: {e}")
        continue

    # Crear objeto BeautifulSoup para analizar el HTML
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    for libro in libros:
        #checar que tengas 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            
            #guardar titulo en varible
            titulo_libro = libro.select("a")[1]["title"]
            rating = libro.p["class"][1]
            precio = libro.select(".price_color")[0].text
            
            #agregar a la lista de libros
            titulos_top.append([titulo_libro, rating, precio])

#Guardas datos en un archivo csv
with open("libros_top.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["N°", "Título", "Rating", "Precio"])
    for i, (titulo, rating, precio) in enumerate(titulos_top, start=1):
        writer.writerow([i, titulo, rating, precio])

# Ver los libros de 4 o 5 estrellas
print("\n Libros con 4 o 5 estrellas:\n")
for i, (titulo, rating, precio) in enumerate(titulos_top, start=1):
    print(f"{i:02d}. {titulo} — {rating} estrellas — {precio}")


#Calcular y mostrar el timepo total de la ejecucion
fin = time.time()
print(f"\n⏱ Tiempo total de ejecución: {fin - inicio:.2f} segundos")
print("Archivo 'libros_top.csv' generado con éxito")