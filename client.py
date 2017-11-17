from socket import *
import sys

try:
	clientSocket = socket(AF_INET, SOCK_STREAM)
except error, msg:
    print 'Socket not created ' + str(msg[0]) + ' ' + str(msg[1])
    sys.exit()

print 'Client created...'
hostname = "192.168.X.X"
clientport = 32849
client_address = (hostname, clientport)
clientSocket.connect(client_address)

while True:
	try:
		while(1):
			message = raw_input('Enter message:')
			# message = 'hello'
			clientSocket.send(str(message))

			data = clientSocket.recv(1024)
			print 'Received data:' + str(data)

	except IOError:
		print 'Error...'

	# finally:
		# clientSocket.close()
