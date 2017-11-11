from socket import *
import sys

try:
	serverSocket = socket(AF_INET, SOCK_STREAM)
except error, msg:
	print 'Socket not created '+ str(msg[0])
	sys.exit()

print 'Server created'

serverPort = 32849
# hostname = 'localhost'
hostname = "0.0.0.0"

print 'hostname is ' + str(hostname)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((hostname, serverPort))

serverSocket.listen(5)

while True:
	print 'Server ready...'

	connectionSocket, addr = serverSocket.accept()
	print connectionSocket, addr

	try:
		while(1):
			message = connectionSocket.recv(1024)
			print 'Message is ', message

			if message:
				message2 = raw_input('Enter message:')
				connectionSocket.sendall(message2)

	except IOError:
		print 'error'

		connectionSocket.close()

serverSocket.close()
