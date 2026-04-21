#extraerá el recuento de comentarios de los datos JSON, calculará la suma de los números en el 
#archivo e ingresará la suma a continuación:
import urllib.request
import json

url = input("") #http://py4e-data.dr-chuck.net/comments_2267909.json

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2267909.json'

op = urllib.request.urlopen(url)
dat = op.read()

info = json.loads(dat)
    #print(info)
comments = info['comments']
total= 0 

for line in comments:
    total += line['count']
    
print(f"Cantidad: {len(comments)}")
print(f"La suma de los count es: {total} ")


