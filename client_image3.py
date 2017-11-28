import socket
import sys
import sys
from socket import *

HOST = '127.0.0.1'
PORT = 6666
size = 100000000

try:
    sock = socket(AF_INET, SOCK_STREAM)
except error, msg:
    print 'Socket not created ' + str(msg[0]) + ' ' + str(msg[1])
    sys.exit()

print 'Client created...'

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)
fname = 'fromserver.png'


def recvall(sock, msgLen):
    msg = ""
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = sock.recv(msgLen - bytesRcvd)

        if chunk == "": break

        bytesRcvd += len(chunk)
        msg += chunk

        if "\r\n" in msg: break
    return msg


try:

    while(1):
        print ("Enter GET to receive image from server")
        message2 = raw_input("Enter message:")
        sock.sendall(message2 + "\r\n")

        if message2 == "GET":
 
            # data = recvall(sock, 4096)

            myfile = open(fname, 'wb')

            amount_received = 0
            while amount_received < size:
                data = recvall(sock, 4096)
                if not data:
                    break
                amount_received += len(data)
                print amount_received

                txt = data.strip('\r\n')

                if 'EOIMG' in str(txt):
                    print 'Image received successfully'
                    myfile.write(data)
                    myfile.close()
                    sock.sendall("DONE\r\n")
                else:
                    myfile.write(data)

        else:

            message = sock.recv(4096)
            print 'Message:' + str(message)

        

finally:
    sock.close()