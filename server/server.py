import time
import sqlite3
from socket import *
import pickle

conn = sqlite3.connect('test.db')
# print("Opened database successfully")

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# accept connection
connectionSocket, addr = serverSocket.accept()
print(connectionSocket.getpeername())

state = 1  # state of whether the program has ended or not


def authenticate(username, password):
    """
    this function authenticates a user
    """
    cursor = conn.execute(
        """SELECT * FROM student WHERE username = (?);""", [username])
    row = cursor.fetchone()
    # if username is found
    if (row):
        dbUsername = row[2]  # get username
        cursor = conn.execute(
            """SELECT * FROM student WHERE username = (?);""", [dbUsername])
        row = cursor.fetchone()
        if (row):
            dbPassword = row[3]  # get password
            # if password matches
            if (dbPassword == password):
                return True
            # if password mismatches
            else:
                return False
    # if username is not found
    else:
        return False


# receive credentials (username, password)
dictionary = connectionSocket.recv(1024)
dictionary = pickle.loads(dictionary)
# verify credentials
validation = authenticate(dictionary["username"], dictionary["password"])
# send validation to client
print(validation)
connectionSocket.send(bytes(validation))

conn.close()  # close database connection

# close socket connection
connectionSocket.close()
