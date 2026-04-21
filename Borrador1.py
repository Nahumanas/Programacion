#Abra el archivo mbox-short.txt y léalo línea por línea. 
#Cuando encuentre una línea que empiece por "From", como la siguiente:
#De stephen.marquard@uct.ac.za , sábado 5 de enero de 2008, 09:14:16
#Analizarás la línea "De" con split() e imprimirás la segunda palabra (es decir, la dirección completa del remitente). 
#Luego, imprimirás un recuento al final.
#Consejo: asegúrese de no incluir las líneas que empiezan por "De:". 
#Consulte también la última línea del ejemplo de salida para ver cómo imprimir el recuento

fname = input('Enter Fname: ')
emails = []

try:
    fh = open('C:/Users/HP/Desktop/Proyecto/Py4e/Estructured Dates/ex_08/mbox-short.txt')
except FileNotFoundError:
    print('No encontrado', fname)
    exit()

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):  # Solo líneas que empiezan con "From "
        words = line.split()
        emails.append(words[1])  # El segundo elemento es el correo

# Imprimir todos los correos en una sola línea, separados por espacio
print(" ".join(emails))







    

    
