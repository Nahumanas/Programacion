fname = input('Enter Fname:')

handle = open('C:/Users/HP/Desktop/Proyecto/Py4e/Estructured Dates/ex_09/mbox-short.txt')
counts = dict()
for line in handle: #recorremos las lineas
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email , 0) + 1
    

bigcount = None
bigword = None
for word , count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword , bigcount)

    
