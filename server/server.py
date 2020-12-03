# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:41:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""
import socket
import threading
import userManaging as user_managing

### global variables
PORT = 7009
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'
# list of all connected IPs with their usernames
allUsers = set(())

"""
Defined on Sun Nov 29 00:44:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: Bind socket to the HOST_INFORMATION and start it to listen
state: 0
"""
def main():
    address = socket.gethostbyname(socket.gethostname())
    HOST_INFORMATION = (address, PORT)

    # make a socket
    # socket.AF_INET == IPv4 PROTOCOL -> our "NETWORK LAYER PROTOCOL"
    # socket.SOCK_STREAM == TCP PROTOCOL -> our "TRANSPORT LAYER PROTOCOL"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(HOST_INFORMATION)

    # Reading from file and then close the file
    with open("users.txt", "r") as usersFile:
        # add all users from users.txt to allUsers set
        for line in usersFile:
            # extra print for checking
            print(line)
            allUsers.add(line)

    print("[SERVER STARTS] Server is starting ...")

    start(s)

"""
Defined on Sun Nov 29 00:53:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: Server creates and starts new thread for each accepted client
state: 0
"""
def start(server):
    server.listen()

    while True:
        conn, addr = server.accept()

        t = threading.Thread(target = user_managing.handle_client, args = (conn, addr))

        t.start()


if __name__ == '__main__':
    main()
