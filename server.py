# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:41:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""
import socket
import threading

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

        t = threading.Thread(target = handle_client, args = (conn, addr))

        t.start()

"""
Defined on Sun Nov 29 01:14:00 2020 (1399/9/9)
@author: Bahar Kaviani
description: set 'connected' flag to 'True' till the client sends "DISCONNECT"
             while the flag is set reads client messages from conn
"""
def handle_client(conn, addr):
    print("[NEW CONNECTION] Client connected from {}".format(addr))
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


if __name__ == '__main__':
    main()
