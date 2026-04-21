# Convertir una lista en tupla
lista = [1, 2, 3]
tupla_desde_lista = tuple(lista)
print(tupla_desde_lista)  # (1, 2, 3)

# Convertir un string en tupla
texto = "Hola"
tupla_desde_string = tuple(texto)
print(tupla_desde_string)  # ('H', 'o', 'l', 'a')

(x , y) = (4 , 6)
print(y)    #generar una tupla de llave y valor
#6

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
    #csev 2
    #cwen4

tups = d.items()
print(tups)
#dict_items([('csev' , 2)] , ('cwen' , 4)])

a = (3, 4)  #Compara 3 con 3 → iguales → sigue

b = (3, 5) #Compara 4 con 5 → 4 < 5 → ✅ entonces a < 

print(a < b)  # ✅ True
