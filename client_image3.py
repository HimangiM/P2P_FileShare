import socket
import sys
import sys
from socket import *

HOST = '192.168.X.X'
PORT = 32849
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
fname1= 'fromserver.wav'
fname2= 'fromserver.txt'

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



print ("Enter TEXT,<image_name> to receive image from server")
print ("Enter IMAGE,<image_name> to receive image from server")
print ("Enter SOUND,<image_name> to receive image from server")


try:

    while(1):
        #print ("Enter IMAGE,<image_name> to receive image from server")
        #print ("Enter SOUND,<image_name> to receive image from server")
        message2 = raw_input("Enter message:")
        fname='2.png'
        txt = message2.strip().split(",")
        # Add if image exists or not
        sock.sendall(message2 + "\r\n")
        
        if txt[0].strip() == "TEXT":
 
            # data = recvall(sock, 4096)
            
            myfile = open(fname2, 'w')

            amount_received = 0
            while amount_received < size:
                data = recvall(sock, 4096)
                if not data:
                    break
                amount_received += len(data)
                print 'Amount received:', amount_received

                txt = data.strip('\r\n')

                if 'EOTXT' in str(txt):
                    print 'TEXT received successfully'
		    data = data[:-7]
                    myfile.write(data)
                    myfile.close()
                    sock.sendall("DONE\r\n")
                    message = sock.recv(4096)
                    print 'Message:' + str(message)
                    break


        elif txt[0].strip() == "IMAGE":
 
            # data = recvall(sock, 4096)
            
            myfile = open(fname, 'wb')

            amount_received = 0
            while amount_received < size:
                data = recvall(sock, 4096)
                if not data:
                    break
                amount_received += len(data)
                print 'Amount received:', amount_received

                txt = data.strip('\r\n')

                if 'EOIMG' in str(txt):
                    print 'Image received successfully'
		    
                    myfile.write(data)
                    myfile.close()
                    sock.sendall("DONE\r\n")
                    message = sock.recv(4096)
                    print 'Message:' + str(message)
                    break

        elif txt[0].strip() == "SOUND":
 
            # data = recvall(sock, 4096)

            myfile = open(fname1, 'wb')

            amount_received = 0
            while amount_received < size:
                data = recvall(sock, 4096)
                if not data:
                    break
                amount_received += len(data)
                print 'Amount received:', amount_received

                txt = data.strip('\r\n')

                if 'EOSND' in str(txt):
                    print 'Sound received successfully'
		    data = data[:-7]
                    myfile.write(data)
                    myfile.close()
                    sock.sendall("DONE\r\n")
                    message = sock.recv(4096)
                    print 'Message:' + str(message)
                    break
                else:
                    myfile.write(data)

        else:
            
            message = sock.recv(4096)
            print 'Message:' + str(message)

        

finally:
    sock.close()
