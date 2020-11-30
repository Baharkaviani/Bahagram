"""
Created on Mon Nov 30 17:43:00 2020 (1399/9/10)
@author: Bahar Kaviani
"""
import socket
import threading
import user as user

# global variables
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'
onlineUsers = set()

"""
Defined on Mon Nov 30 18:26:00 2020 (1399/9/10)
@author: Bahar Kaviani
description:
end: no
"""
def register(username):


"""
Defined on Sun Nov 29 01:14:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: set 'connected' flag to 'True' till the client sends "DISCONNECT"
             while the flag is set reads client messages from conn
end: no
"""
def handle_client(conn, addr):
    print("[NEW CONNECTION] Client connected from {}".format(addr))
    connected = True

    # print all online users for the new connected user
    for o in onlineUsers:
        print(o)

    # add connected user to the onlineUsers set
    onlineUsers.add()

    # recieve the message from Client
    while connected:
        message_length = int(conn.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        msg = conn.recv(message_length).decode(ENCODING)

        print("[MESSAGE RECIEVED] {}".format(msg))

        if msg == "DISCONNECT":
            connected = False

    # if connected == false "while" ends and connection will be closed
    conn.close()
