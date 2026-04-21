name = input('Enter file:') 
handle = open(name) #abrimos

counts = dict() #diccionario vacio (creamos)
for line in handle: #recorremos el file
    words = line.split() #Divide las lineas (muchas)
    for word in words: #para cada palabra de la linea, las haremos una al vez
        counts[word] = counts.get(word , 0) +1 #Cada linea contala, si se repiete sumale 1 
#Tenemos un Diccionario y un Histograma.

bigcount = None  #Lo igualamos a NADA
bigword = None   #Queremos encontrar la palabra y el conteo mas grande.
for word, count in counts.items(): #Producimos un bucle maximo definido
    if bigcount is None or count > bigcount: 
        bigword = word #El big es mas grande que el mayor (word)
        bigcount = count

#Prin(bigword,bigcount)
