#Utilizacion de BEATIFUL SHOP

import urllib.request , urllib.parse , urllib.error

from bs4 import BeautifulSoup

url = input("Enter - ")
#Insertar URL (direccion de la pag)

html = urllib.request.urlopen(url).read() 
#Genera que lea todo la pagina hasta las nuevas lienas

soup = BeautifulSoup(html , 'html.parser')
#Le pedimos que lo analice 

#Recuperar todas las etiquetas de anclaje

tags = soup('a')
for tag in tags:
    print(tag.get('href' , None))
    
#urllib.request: para hacer solicitudes HTTP #Sirve para abrir URLs, descargar contenido o interactuar con APIs
#urllib.parse: para manipular URLs #Te permite dividir, construir o modificar URLs fácilmente.
#urllib.error: para manejar errores de red #Define excepciones como HTTPError y URLError, que te ayudan a capturar fallos al hacer solicitudes.
