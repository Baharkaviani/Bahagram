# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:41:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""
import socket
import threading
import userHandling as handle

PORT = 7009
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'

"""
Defined on Sun Nov 29 00:44:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: bind socket to the HOST_INFORMATION and start it to listen
"""
def main():
    address = socket.gethostbyname(socket.gethostname())
    HOST_INFORMATION = (address, PORT)

    # make a socket
    # socket.AF_INET == IPv4 PROTOCOL -> our "NETWORK LAYER PROTOCOL"
    # socket.SOCK_STREAM == TCP PROTOCOL -> our "TRANSPORT LAYER PROTOCOL"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(HOST_INFORMATION)

    print("[SERVER STARTS] Server is starting ...")

    start(s)

"""
Defined on Sun Nov 29 00:53:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: server creates and starts new thread for each accepted client
"""
def start(server):
    server.listen()

    while True:
        conn, addr = server.accept()

        t = threading.Thread(target = handle.handle_client, args = (conn, addr))

        t.start()


if __name__ == '__main__':
    main()
