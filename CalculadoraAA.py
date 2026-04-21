#voy a generar otra calculadora para practicar. 

print("Bienvenido a una calculadora de pratica")
print("Al hacer la operacion acepta sum , res , div , multi")
print("Para salir escriba nono")
numeros = ''
ecuacion = ''
segundo = ''

while True:
    if not numeros:
        numero = input("Ingrese el primer numero : ")
        if numero.lower() == 'nono': 
            break 
        numero = int(numero) 
    ecuacion = input("Ingrese el nombre de la ecuacion : ")
    if ecuacion.lower()  == 'nono' : 
            break
    segundo = input("Ingrese el segundo numero : ")
    if segundo.lower()== "nono":
        break 
    segundo = int(segundo)
        
    if ecuacion.lower() == 'sum':
        numero += segundo
    elif ecuacion.lower() == 'res':
        numero -= segundo
    elif ecuacion.lower() == 'multi' :
        numero *= segundo
    elif ecuacion.lower() == 'div' : 
        numero /= segundo
    else: 
        print("Ecuacion incorrecta")
        break

    print(f"Su resultado es : {numero}")
