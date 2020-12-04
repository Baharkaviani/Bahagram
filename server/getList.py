"""
Created on Fri Dec 4 18:44:00 2020 (1399/9/14)
@author: Bahar Kaviani
description:
# TODO: add this file to commands folder
'''
commands:
    getList->AllUsernames
"""
import socket
import threading
import user as User
import userInformation as user_information

### global variables
PORT = 7009
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'
# connection information
CONN = None

"""
Defined on Fri Dec 4 18:58:00 2020 (1399/9/14)
description: Prepare different choices for the user who wants to see a list off users
"""
def get_list(conn, command):
    global CONN
    CONN = conn
    
    if command == "AllUsernames":
        getAllUsernames()
    else:
        pass

"""
Defined on Fri Dec 4 19:23:00 2020 (1399/9/14)
description: Send all user names to client
"""
def getAllUsernames():
    send_msg("[LIST OFF ALL USERS]")

    for u in user_information.allUsers:
        uName = u.username
        send_msg(uName)

"""
Defined on Sun Nov 29 02:34:00 2020 (1399/9/9)
description: for each message first send message length then send the message
"""
def send_msg(msg):
    message = msg.encode(ENCODING)

    msg_length = len(message)
    msg_length = str(msg_length).encode(ENCODING)
    # check if the msg_length is shorter then 64 byte
    msg_length += b' ' * (MESSAGE_LENGTH_SIZE - len(msg_length))

    CONN.send(msg_length)
    CONN.send(message)
