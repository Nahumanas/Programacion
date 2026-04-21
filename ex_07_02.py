#7.2 Write a program that prompts for a file name
# then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

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

if count > 0: #Al estar afuera del bucle produce que solo imprima una
   promedio = total / count
   print('Average spam confidence:' , promedio)

