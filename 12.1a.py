import socket
# Conexion con la red 

mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
# Apertura (abre la conexion)
#AF_INET: protocolo IPv4
#SOCK_STREAM: tipo de conexión TCP (fiable, orientada a conexión)

mysock.connect(('data.pr4e.org' , 80))
# Se conecta al servidor en la puerta 80

cmd = 'GET/romeo.txt HTTP/1.0\r\n\n'.encode()
#GET: método para solicitar datos
#HTTP/1.0: versión del protocolo
#\r\n\n: indica el final del encabezado HTTP
#.encode(): convierte el texto en bytes para enviarlo por el socket

mysock.send(cmd)
#Envía el comando al servidor.

while True:
    data = mysock.recv(512)
    if (len(data)< 1 ):
        break
    print(data.decode())
mysock.close()