# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 02:12:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""

import socket

PORT = 7009

MESSAGE_LENGTH_SIZE = 64

ENCODING = 'utf-8'

"""
Defined on Sun Nov 29 02:17:00 2020 (1399/9/9)
@author: Bahar Kaviani
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

    # get first message from console and send it to server
    first_msg = input()
    send_msg(s, first_msg)
    send_msg(s, "DISCONNECT")

"""
Defined on Sun Nov 29 02:34:00 2020 (1399/9/9)
@author: Bahar Kaviani
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
    

if __name__ == '__main__':
    main()
