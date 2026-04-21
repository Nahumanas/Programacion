#Dictionary and List

#Patron de Conteo
count = dict()
print('Enter a line of text:')   #El patrón general para contar las palabras en una línea de texto es dividir la línea en palabras,                                   ç
                                 #Luego recorrer las palabras y                                 .
line = input(' ')
words = line.split()

print('Wrods:' , words) #Usar un diccionario para rastrear el recuento de cada palabra de forma independiente

print('Counting..')
for word in words:
    count[word] = count.get(word,0) + 1
print('Count' , count)

#Loops and Dictionaries
print('LOOPS')
counts = {'chuck': 1 , 'fred' : 42 , 'jan' : 100}
for key in counts:
    print(key, counts[key])   #Leer el diccionario y da sus valores

#List of Keys and Values
print('LIST')

jjj = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
print(list(jjj)) #Lista rta= ['chuck' , 'fred' , 'jan']

print(list(jjj.keys())) #realmente estas llamando el codigo del diccionario.

print(list(jjj.values())) #[1 , 42 , 100] los valores de las llaves en una lista

print(list(jjj.items())) #[(chuck , 1 ), (fred , 42) , (jan , 100)] #TUPLA se llama
#Con este ultimo es imprimir todo