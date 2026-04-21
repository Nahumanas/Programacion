fname = input("Enter fname:")
fn = open('C:/Users/HP/Desktop/Proyecto/Py4e/Estructured Dates/ex_07_01_07_02/mbox-short.txt')
count = 0
total = 0.0
for lc in fn: #este comando lo que hace es leer todo para poder imprimirlo , no lo tengo que repetir
 if not 'X-DSPAM-Confidence:' in lc:
   continue
 count = count +1   
 corte = lc.find(':') #posicion 18
 flotante = lc [corte+2:].strip()
 value = float(flotante)
 total = total + value
    
if count > 0 :
   promedio = total / count
   print('Average spam confidence:' , promedio)




      
      

