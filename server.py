from socket import *

serverPort = 12456

serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',12456))

print ('The server is connected')


while 1:
	
number1,  clientAddress  = serverSocket.recvfrom(2048)
	
calc, 	  clientAddress  = serverSocket.recvfrom(2048)	
	
number2,  clientAddress	 = serverSocket.recvfrom(2048)



if calc == '+':
	modifiedAddition = int(number1.decode()) + int(number2.decode())
	
modifiedAddition = str(modifiedAddition)
	
serverSocket.sendto(modifiedAddition.encode(), clientAddress)
	
print('You added up numbers')

else: 
	pass



if calc == '-':
	modifiedAddition = int(number1.decode()) - int(number2.decode())
	
modifiedAddition = str(modifiedAddition)
	
serverSocket.sendto(modifiedAddition.encode(), clientAddress)
	
print ('You have succesfully subtracted')

else:
	pass
 
