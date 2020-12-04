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
description: Set 'connected' flag to 'True' till the client sends "DISCONNECT"
    while the flag is set reads client messages from conn
end: no
"""
def handle_client(conn, addr):
    print("[NEW CONNECTION] Client connected from {}".format(addr))

    # # extra print for checking
    # print("[userInformation]: ")
    # for obj in user_information.allUsers:
    #    print( obj.IP, obj.username, sep =' ' )

    # extra print for checking
    print("[check if client is new]: {}".format(checkIP(addr)))

    isNew = checkIP(addr)

    if isNew:
        register()
    else:
        pass

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

    # check all connected users' IP addresses
    for user in user_information.allUsers:
        if IP == user.IP:
            return True

    return False

"""
Defined on Fri Dec 3 03:56:00 2020 (1399/9/14)
description: Check if the username is new or not
"""
def checkUsername(username):
    # check all connected users' usernames
    for user in user_information.allUsers:
        if username == user.IP:
            return True

    return False


"""
Defined on Mon Nov 30 18:26:00 2020 (1399/9/10)
description: Ask username from new user.
    Save the IP and the username to users.txt file
end: no
"""
def register(address):

    checkUsername()

    with open("users.txt", "w") as usersFile:
        usersFile.write(address + ":" + username)
