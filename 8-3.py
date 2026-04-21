#Listas y Cadenas (Strings and List)
abc = 'With three words'
stuff = abc.split() #A dicha variable lo parte en 3
print(stuff)
print(len(stuff)) #longitud = 3
print(stuff[0]) #Extraer una palabra
for w in stuff:
    print(w)    #Y asi lo transformo en un bucle
                #Imprime 3 veces


fhand = open('C:/Users/HP/Desktop/Proyecto/Py4e/Estructured Dates/ex_08/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From') : continue
    words = line.split()
    print(words)