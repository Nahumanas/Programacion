import urllib.request, urllib.parse, urllib.error
# 📦 Importa módulos para manejar URLs:
# - request: para abrir URLs
# - parse: para codificar/decodificar parámetros
# - error: para manejar errores al acceder a URLs

from bs4 import BeautifulSoup
# 🍜 Importa BeautifulSoup, la librería que permite analizar y extraer datos de HTML

import ssl
# 🔐 Importa el módulo SSL para manejar certificados de seguridad (HTTPS)

# 🛠️ Crea un "contexto" SSL que ignora errores de certificados (útil para sitios con certificados vencidos o mal configurados)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 🖥️ Pide al usuario que ingrese una URL
url = input("Enter - ")

# 🌐 Abre la URL ingresada, usando el contexto SSL para evitar errores de certificado
html = urllib.request.urlopen(url, context=ctx).read()  #Un archivo abierto (file-like object) ✅ devuelve

# 🍲 Crea el objeto BeautifulSoup para analizar el HTML descargado
soup = BeautifulSoup(html, 'html.parser')

# 🔍 Busca todas las etiquetas <a> (enlaces) dentro del HTML
tags = soup('a')

# 🔗 Recorre cada etiqueta <a> y muestra el valor del atributo 'href' (el enlace)
for tag in tags:
    print(tag.get('href', None))
