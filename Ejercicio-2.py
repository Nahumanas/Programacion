#Busca el enlace en la posición 18 (el primer nombre es 1). Sigue ese enlace. Repite este proceso 7 veces. 
#La respuesta es el apellido que recuperas.
#Pista: El primer carácter del nombre de la última página que cargarás es: C
# http://py4e-data.dr-chuck.net/known_by_Gene.html
import urllib.request , urllib.parse , urllib.error
import re 

from bs4 import BeautifulSoup
import ssl 

ctx= ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")

repeticion = int(input("Cantidad de bucles : "))

posicion = int(input("Ingrese la posicion: ")) -1 

for tag in range(repeticion): 
    print("Recuperando:", url)
    html = urllib.request.urlopen(url , context = ctx).read()
    soup = BeautifulSoup(html , 'html.parser')
    tags = soup("a")
    nombre = tags[posicion].get('href' , None)
    url = nombre 

print(f"La respuesta de la tarea es {tags[posicion].text}")