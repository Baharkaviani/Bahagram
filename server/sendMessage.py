"""
Created on Fri Dec 4 14:38:00 2020 (1399/9/14)
@author: Bahar Kaviani
description:
# TODO: add this file to commands folder
"""
import socket
import threading
import user as User
import userInformation as user_information

### global variables
PORT = 7009
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'

def toPerson():
    print("[send message to toPerson]")
