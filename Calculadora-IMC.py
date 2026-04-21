print("BIENVENIDO A LA CALCULADORA DE IMC")
print("Su peso debe ponerlo en numero entero y su talla la debe poner en metro (m)")
print("Para salir escriba exit")
print('Escriba realizar , para que se haga la cuenta')

peso = ''
talla = ''
IMC = ''

while True:
    if not peso:
     peso = input('Ingrese su peso : ')
     if peso.lower() == 'exit' : 
         break
     peso = int(peso)
     
     if not talla:
      talla = input('Ingrese su talla : ')
     if talla.lower() == 'exit' : 
        break
     talla = float(talla)
    if not IMC : 
        IMC = input('Realice la cuenta : ')
        if IMC.lower() == 'exit' : 
         break
    
    if IMC.lower() == 'realizar' : 
       IMC = peso/ (talla**2)
    else: 
        print('No valido , verifica los datos')
    break
print(f"Tu resultado de IMC es : {IMC}")
    

     
    
    

    

