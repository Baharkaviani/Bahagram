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
import sendMessage as send_message
import getList as get_list

### global variables
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'
# connection information
CONN = None
ADDR = None

"""
Defined on Sun Nov 29 01:14:00 2020 (1399/9/9)
description: Set 'connected' flag to 'True' till the client sends "DISCONNECT"
    while the flag is set reads client messages from conn
"""
def handle_client(conn, addr):
    global CONN
    global ADDR
    CONN = conn
    ADDR = addr

    print("[NEW CONNECTION] Client connected from {}".format(ADDR))

    # extra print for checking
    print("[userInformation]: ")
    for obj in user_information.allUsers:
       print( obj.IP, obj.port, obj.username)

    # check if the connected client is a new user or not
    isNew = checkIP()

    if isNew:
        register()
    else:
        sendHelloToClient()
        getCommand()

"""
Defined on Fri Dec 4 20:58:00 2020 (1399/9/14)
description: Send Hello to client
"""
def sendHelloToClient():
    IP = ADDR[0]
    for user in user_information.allUsers:
        if IP == user.IP:
            username = user.username

    msg = "Hello {}".format(username)
    message = msg.encode(ENCODING)

    msg_length = len(message)
    msg_length = str(msg_length).encode(ENCODING)
    # check if the msg_length is shorter then 64 byte
    msg_length += b' ' * (MESSAGE_LENGTH_SIZE - len(msg_length))

    CONN.send(msg_length)
    CONN.send(message)

"""
Defined on Thu Dec 3 20:33:00 2020 (1399/9/13)
description: Check if the IP address is new or not
"""
def checkIP():
    IP = ADDR[0]

    isNew = True

    # check all connected users' IP addresses
    for user in user_information.allUsers:
        if IP == user.IP:
            isNew = False

    return isNew

"""
Defined on Fri Dec 4 03:56:00 2020 (1399/9/14)
description: Check if the username is new or not
"""
def checkUsername(username):
    isNew = True

    # check all connected users' usernames
    for user in user_information.allUsers:
        if username == user.username:
            isNew = False

    return isNew

"""
Defined on Mon Nov 30 18:26:00 2020 (1399/9/10)
description: Ask username from new user.
    Save the IP, port and the username to users.txt file
    After registering user can send commands to server.
"""
def register():

    # TODO: add a function to ask client it's username
    #       now we just consider that the first sent data is user's username
    #       the username will be checked by checkUsername function if it is new or not

    usernameIsNew = False

    # recieve the message from Client
    while usernameIsNew == False:
        username_length = int(CONN.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        username = CONN.recv(username_length).decode(ENCODING)

        print("[USERNAME RECIEVED] {}".format(username))

        usernameIsNew = checkUsername(username)

    # write user information to the "users.txt" file and add to the user_information.allUsers
    user_information.addUser(ADDR[0], ADDR[1], username)

    # now user can send command
    getCommand()

"""
Defined on Fri Dec 4 15:05:00 2020 (1399/9/14)
description: Gets the user command then find the proper function for that
"""
def getCommand():
    # set the connected flag to True until client sends "DISCONNECT"
    connected = True

    # recieve the message from Client
    while connected:
        message_length = int(CONN.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        msg = CONN.recv(message_length).decode(ENCODING)

        print("[MESSAGE RECIEVED] {}".format(msg))

        # TODO: make a new function for managing these if clauses
        if msg == "getList":
            # send the next command to get_list function
            print("[getList COMMAND RECIEVED] {}".format(msg))
            get_list.get_list(CONN, msg)

        if msg == "DISCONNECT":
            connected = False

    # if connected == false "while" ends and connection will be closed
    CONN.close()
