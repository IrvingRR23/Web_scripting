import bs4
import requests

#Crear una url sin numero de pagina
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

#lista de titulos con mas de 4 estrellas
titulos_top = []

for pagina in range (1,51):
    #Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select(".product_pod")
    for libro in libros:
        #checar que tengas 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            
            #guardar titulo en varible
            titulo_libro = libro.select("a")[1]["title"]
            
            #agregar a la lista de libros
            titulos_top.append(titulo_libro)

# Ver los libros de 4 o 5 estrellas
print("\n Libros con 4 o 5 estrellas:\n")
for i, titulo in enumerate(titulos_top, start=1):
    print(f"{i:02d}. {titulo}")
