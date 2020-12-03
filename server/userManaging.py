"""
Created on Mon Nov 30 17:43:00 2020 (1399/9/10)
@author: Bahar Kaviani
description: Manage users when they request to connect the server.
    Check if the user is new or not by it's IP address.
    If it was get username.
"""
import socket
import threading
import userInformation as user_information

### global variables
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'

"""
Defined on Sun Nov 29 01:14:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: Set 'connected' flag to 'True' till the client sends "DISCONNECT"
    while the flag is set reads client messages from conn
end: no
"""
def handle_client(conn, addr):
    print("[NEW CONNECTION] Client connected from {}".format(addr))

    # extra print for checking
    print(user_information.allUsers)

    connected = True

    # recieve the message from Client
    while connected:
        message_length = int(conn.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        msg = conn.recv(message_length).decode(ENCODING)

        print("[MESSAGE RECIEVED] {}".format(msg))

        if msg == "DISCONNECT":
            connected = False

    # if connected == false "while" ends and connection will be closed
    conn.close()

"""
Defined on Mon Nov 30 18:26:00 2020 (1399/9/10)
@author: Bahar Kaviani
description:
end: no
"""
def register(username):
    pass
