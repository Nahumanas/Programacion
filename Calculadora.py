#Calculadora
#Para salir escriba exit
print('Bienvenido a la Calculadora')

print('Para salir escriba exit')

print('Las operaciones son suma , resta , multi y div')

resultado = ""
while True:
    if not resultado:
         resultado = input('Ingrese el numero: ')
         if resultado.lower == 'exit':
              break
         resultado = int(resultado)
    op = input('Ingrese la operacion: ')
    if op.lower() == 'exit':
        break
    n2 = input('Siguiente Numero:')
    if n2.lower() == 'exit':
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "div":
        resultado /= n2
    elif op.lower() == "multi":
        resultado *= n2
    else:
        print("Operacion no valida")
        break
    
    print(f"El resultado es {resultado}")

    
    
    