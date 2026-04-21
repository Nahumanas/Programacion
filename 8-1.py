print(range(4)) #0 ,1 , 2 , 3
friends = ['Joseph','Glenn', 'Sally']
print(len(friends)) #Esto imprime la cantidad de elementos en la lista
print(list(range(len(friends)))) #Cuando hablamos de índices en una lista
#estamos señalando la posición de cada elemento dentro de esa lista

for friend in friends : 
    print('Happy New Year:' , friend) #Imprimir la lista correspondiente 
for i in range(len(friend)):
    friend = friends[0] #Con este bucle lo que hacemos es imprimir solo el indiaco (0 , 1 , 2) y esto lo imprime 
    print('Happy New Year:' , friend)