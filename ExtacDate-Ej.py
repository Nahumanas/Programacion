import re 

hand = open('C:/Users/HP/Desktop/Proyecto/Py4e/Access Dates in the Web/mbox-short.txt')

lst = list()

for line in hand : 
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    lst.append(num)

print("Valores Encontrados" , lst)
print( "Maximun:" , max(lst) )