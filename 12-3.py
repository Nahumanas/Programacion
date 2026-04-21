
import socket
while True:
    data = mysock.recv(512)
    if ( len(data) < 1):
        break
    mystring = data.decode() 
    print(mystring)
#data.decode dice "Yo resuelvo esto "
#Es para saber que tipo de decodifcante utiliza, 
#Dichpo archivo. (UTF-8 , UTF-16 o ASCII)

import socket

mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org' , 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#Encode codifica adecuadamente en UTF-8 para enviarlo
