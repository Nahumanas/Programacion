fname = input("Enter Fname:")
lst = list()
fh= open('C:/Users/HP/Desktop/Proyecto/Py4e/Estructured Dates/ex_08/romeo.txt')

for line in fh:
    line = line.strip()
    lineas = line.split()
    for palabra in lineas:
        if palabra not in lst:
         lst.append(palabra)
lst.sort()
print(lst)








    

    
