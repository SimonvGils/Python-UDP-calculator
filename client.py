from socket import * 
serverName = 'Localhost'
serverport = 12456
clientSocket = socket(AF_INET, SOCK_DGRAM)



number1 = raw_input('Input number1: ')
calc = raw_input('Calculation: +, - ,/ ,*: ')
number2 = raw_input('Input number2: ')

clientSocket.sendto(number1.encode(),('Localhost',12456))
clientSocket.sendto(calc,('Localhost',12456))
clientSocket.sendto(number2.encode(),('Localhost',12456))

modifiedAddition, serverAddress=clientSocket.recvfrom(2048)
print(modifiedAddition.decode())
clientSocket.close()
