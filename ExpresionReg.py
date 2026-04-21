#hand = open('C:/Users/HP/Desktop/Proyecto/Py4e/Access Dates in the Web/mbox-short.txt')

#for line in hand:
    #line = line.strip()
    #if line.find("From:") >= 0:
     #   print(line)
    
import re #BIBLIOTECA  
hand = open('C:/Users/HP/Desktop/Proyecto/Py4e/Access Dates in the Web/mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search("From:" , line) : 
        print(line)
            