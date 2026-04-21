import urllib.request
import xml.etree.ElementTree as ET

url = input("Ingrese la URL: ")

if len (url) < 1 : #“Si el usuario no ingresó ninguna URL, usá esta URL por defecto para seguir trabajando.”
    url = 'https://py4e-data.dr-chuck.net/comments_2267908.xml'

op = urllib.request.urlopen(url)
data = op.read()

tree = ET.fromstring(data)
lsn = tree.findall('comments/comment') #Sin espacio extra!
count = 0

print("Cantidad de count" , len(lsn))

for line in lsn:
    count += int(line.find('count').text)

print(f"Su suma es de : {count}") 
    