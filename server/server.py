from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# accept connection
connectionSocket, addr = serverSocket.accept()
print(connectionSocket.getpeername())

state = 1 # state of whether the program has ended or not

import time
timeout = time.time() + 60 * 1   # 5 minutes from now
while True:
    if time.time() > timeout:
        break

# close connection
connectionSocket.close()