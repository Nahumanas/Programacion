import re 

hl = open("C:/Users/HP/Desktop/PY/Py4e/Access Dates in the Web/M1/regex_sum_42.txt")
count = 0
total = 0

for line in hl: 
    line = line.rstrip()
    stuff = re.findall('[0-9]+' , line)
    if not stuff : continue 
    count += len(stuff) 
    for suma in stuff:
        total+= int(suma) 


print(f"La cantidad de caracteres son : {count}")
print(f"El total de la suma es : {total}")