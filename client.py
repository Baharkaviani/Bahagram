# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 02:12:00 2020 (1399/9/9)
@author: Bahar Kaviani
"""

import socket

PORT = 9797

MESSAGE_LENGTH_SIZE = 64

ENCODING = 'utf-8'

def main():
    address = socket.gethostbyname(socket.gethostname())
    SERVER_INFORMATION = (address, PORT)

    # make a socket
    # socket.AF_INET == IPv4 PROTOCOL -> our "NETWORK LAYER PROTOCOL"
    # socket.SOCK_STREAM == TCP PROTOCOL -> our "TRANSPORT LAYER PROTOCOL"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(SERVER_INFORMATION)

    send_msg(s, "Hello Bahar :D")
    send_msg(s, "DISCONNECT")

def send_msg(client, msg):
    message = msg.encode(ENCODING)

    msg_length = len(message)
    msg_length = str(msg_length).encode(ENCODING)
    msg_length += b' ' * (MESSAGE_LENGTH_SIZE - len(message_length))

    client.send(msg_length)
    client.send(message)


if __name__ == '__main__':
    main()
