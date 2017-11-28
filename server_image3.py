import random
import socket, select
from time import gmtime, strftime
import sys
from socket import *

image = '1.png'

HOST = '127.0.0.1'
PORT = 6666

connected_clients_sockets = []

try:
    server_socket = socket(AF_INET, SOCK_STREAM)
except error, msg:
    print 'Socket not created '+ str(msg[0])
    sys.exit()

print 'Server created'

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)


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


while True:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

        else:
            try:
                while(1):
                    data = recvall(sock, 4096)

                    if data:
                        print 'Message:', data.strip("\r\n")
                        txt = data.strip()

                        if txt == 'GET':
                            
                            with open(image, 'rb') as f1:    
                                file_size = len(f1.read())
                                f1.seek(0)

                            with open(image, 'rb') as fp:
                                image_data = fp.read()

                            msg = '%sEOIMG\r\n' % image_data
                            # msg = str(file_size) + "," + str(image_data) + 'EOIMG\r\n'

                            sock.sendall(msg)

                        else:                    
                            message  = raw_input("Enter message:")
                            sock.sendall(message)

            except:
                sock.close()
                connected_clients_sockets.remove(sock)
                continue

server_socket.close()