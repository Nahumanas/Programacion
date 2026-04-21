#CONTAR con DICCIONARIOS:
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
#{'csev': 1, 'cwen': 1}
ccc['cwen'] = ccc['cwen'] +1
print(ccc)
#{'csev': 1, 'cwen': 2} basicamente que el cwen aparecio dos veces 

print('cve' in  ccc) #(diccionario) con esto la respuesta es true o false

counts = dict()
names = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen'] #creamos las llaves
for name in names: #leeme los nombres (creando un bucle )
    if name not in counts:# Si el nombre no está en el diccionario...
        counts[name] = 1  #...lo agregamos con valor 1 (primera vez que aparece)
    else:
        counts[name] = counts[name] + 1 # Si el nombre ya está en el diccionario...
print(counts)   # ...sumamos 1 al valor actual (ya apareció antes)
#{'csev': 2, 'cwen': 2, 'zqian': 1} (rta)


alimentos = ['manzana', 'banana', 'manzana'] #lista
calorias = {'manzana': 95, 'banana': 105} #Diccionario

total = 0
for fruta in alimentos:
    print(fruta, calorias.get(fruta, 'No disponible')) #Imprimir el valor individual.
conteo = {}

for fruta in alimentos:
    conteo[fruta] = conteo.get(fruta, 0) + 1  # Contás cuántas veces aparece

print("Conteo por alimento:", conteo)

for fruta in alimentos:
    total += calorias.get(fruta, 0)  # Si no está, suma 0 #Al igualarlo con el total se cuenta todo.

print(total)  # → 295 suma 95 + 95 + 105
