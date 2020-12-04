# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 02:12:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""

import socket

### global variables
PORT = 7009
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'

"""
Defined on Sun Nov 29 02:17:00 2020 (1399/9/9)
description: connect socket to the SERVER_INFORMATION and send a message
"""
def main():
    address = socket.gethostbyname(socket.gethostname())
    SERVER_INFORMATION = (address, PORT)

    # make a socket
    # socket.AF_INET == IPv4 PROTOCOL -> our "NETWORK LAYER PROTOCOL"
    # socket.SOCK_STREAM == TCP PROTOCOL -> our "TRANSPORT LAYER PROTOCOL"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(SERVER_INFORMATION)

    message_length = int(s.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
    msg = s.recv(message_length).decode(ENCODING)

    print(msg)

    # get first message from console and send it to server
    while True:
        first_msg = input()
        send_msg(s, first_msg)

"""
Defined on Sun Nov 29 02:34:00 2020 (1399/9/9)
description: for each message first send message length then send the message
"""
def send_msg(client, msg):
    message = msg.encode(ENCODING)

    msg_length = len(message)
    msg_length = str(msg_length).encode(ENCODING)
    # check if the msg_length is shorter then 64 byte
    msg_length += b' ' * (MESSAGE_LENGTH_SIZE - len(msg_length))

    client.send(msg_length)
    client.send(message)

"""
Defined on Fro Dec 4 19:10:00 2020 (1399/9/14)
description:
"""
def check_msg(command):
    if command == "getList":
        receiving = True

        # recieve the message from Client
        while receiving:
            message_length = int(CONN.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
            msg = CONN.recv(message_length).decode(ENCODING)

            print(msg)

            if msg == "END":
                receiving = False

if __name__ == '__main__':
    main()
