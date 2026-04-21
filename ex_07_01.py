file = input("Enter File:")
fh =  open("C:/Users/HP/Desktop/Proyecto/Py4e/Estructured Dates/ex_07_01/words.txt") #Indication in the file

for lx in fh:
    ly = lx.upper() #IN Mayus
    ld = ly.rstrip()#Delete in the space white
    print(ld)
   

  
