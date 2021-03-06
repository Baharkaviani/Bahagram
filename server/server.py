# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:41:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""
import socket
import threading
import managing as managing
import userInformation as user_information

### global variables
PORT = 7009

"""
Defined on Sun Nov 29 00:44:00 2020 (1399/9/9)
description: Bind socket to the HOST_INFORMATION and start it to listen
"""
def main():
    address = socket.gethostbyname(socket.gethostname())
    HOST_INFORMATION = (address, PORT)

    # make a socket
    # socket.AF_INET == IPv4 PROTOCOL -> our "NETWORK LAYER PROTOCOL"
    # socket.SOCK_STREAM == TCP PROTOCOL -> our "TRANSPORT LAYER PROTOCOL"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(HOST_INFORMATION)

    # Read from file and then close the file
    user_information.initializeAllUsers()

    # start the server
    print("[SERVER STARTS] Server is starting ...")

    start(s)

"""
Defined on Sun Nov 29 00:53:00 2020 (1399/9/9)
description: Server creates and starts new thread for each accepted client
"""
def start(server):
    server.listen()

    while True:
        conn, addr = server.accept()

        t = threading.Thread(target = managing.handle_client, args = (conn, addr))

        t.start()


if __name__ == '__main__':
    main()
