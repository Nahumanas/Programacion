import re 

x = "My 2 favorite numbers are 19 and 42"

y = re.findall('[0-9]+' , x)  #Imprime los numeros

#Con el + = mas de un digito

#print(y)

import re 

j = "From: Using the: character"

i = re.findall('^F.+?:' , j) #Forma corta

#print(i)

import re 
w = 'From stephen.marquiard@uct.ac.za Sat Juan 5 09:141:16 2008'

o = re.findall('@([^ ]*)' , w)
print(o)