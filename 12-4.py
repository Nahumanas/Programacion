#RECUPERACION DE PAG-WEB

import urllib.request , urllib.parse , urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand: 
    print(line.decode().strip())

#Mayormente salta los encabezados pero no es algo que nos interese
#Tratarlo como un archivo web.
#Si es web HTML solo decirselo con .htm al final

#Seguir otro enlaces 

import urllib.request , urllib.parse , urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand: 
    print(line.decode().strip())
    
    #<h1>The Fist Page </h1> 
    #<p>If you like , you can switch to the <a>
href = "http://www.dr_chuck.com/page2.htm">Second
    #Page</a>.
    #</p> 