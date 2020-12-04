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
# TODO: make CONN and ADDR Global

"""
Defined on Sun Nov 29 01:14:00 2020 (1399/9/9)
description: Set 'connected' flag to 'True' till the client sends "DISCONNECT"
    while the flag is set reads client messages from conn
end: no
"""
def handle_client(conn, addr):
    print("[NEW CONNECTION] Client connected from {}".format(addr))

    # extra print for checking
    print("[userInformation]: ")
    for obj in user_information.allUsers:
       print( obj.IP, obj.username)

    # # extra print for checking
    # print("[check if client is new]: {}".format(checkIP(addr)))

    # check if the connected client is a new user or not
    isNew = checkIP(addr)

    if isNew:
        register(conn, addr)
    else:
        pass

    # set the connected flag to True until client sends "DISCONNECT"
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
Defined on Thu Dec 3 20:33:00 2020 (1399/9/13)
description: Check if the IP address is new or not
"""
def checkIP(address):
    IP = address[0]

    isNew = True

    # check all connected users' IP addresses
    for user in user_information.allUsers:
        # # extra print for checking
        # print("[IP address]: {}".format(IP))
        # print("[user.IP:] {}".format(user.IP))
        if IP == user.IP:
            isNew = False

    return isNew

"""
Defined on Fri Dec 3 03:56:00 2020 (1399/9/14)
description: Check if the username is new or not
"""
def checkUsername(username):
    isNew = True

    # check all connected users' usernames
    for user in user_information.allUsers:
        if username == user.username:
            # extra print for checking
            print("[check username]: {}".format(True))
            isNew = False

    return isNew

"""
Defined on Mon Nov 30 18:26:00 2020 (1399/9/10)
description: Ask username from new user.
    Save the IP and the username to users.txt file
end: no
"""
def register(conn, addr):

    # TODO: add a function to ask client it's username
    #       now we just consider that the first sent data is user's username
    #       the username will be checked by checkUsername function if it is new or not

    usernameIsNew = False

    # recieve the message from Client
    while usernameIsNew == False:
        username_length = int(conn.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        username = conn.recv(username_length).decode(ENCODING)

        print("[USERNAME RECIEVED] {}".format(username))

        usernameIsNew = checkUsername(username)

    # weite to the "users.txt" file and then close the file
    with open("users.txt", "a") as usersFile:
        # TODO: ADD user to the user_information.allUsers
        #       first write a function in userInformation file
        usersFile.write(addr[0] + ":" + username)
        usersFile.write("\n")
