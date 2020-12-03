"""
Created on Mon Nov 30 18:50:00 2020 (1399/9/10)
@author: Bahar Kaviani
"""
import socket
import threading

# global variables
MESSAGE_LENGTH_SIZE = 64
ENCODING = 'utf-8'
CONNECTED = False
# list of all connected IPs with their usernames
allUsers = set()

"""
Defined on Thu Dec 3 18:06:00 2020 (1399/9/13)
@author: Bahar Kaviani
description: add all users from users.txt to allUsers set
"""
def initializeAllUsers():
    # Reading from file and then close the file
    with open("users.txt", "r") as usersFile:
        for line in usersFile:
            # extra print for checking
            print("users.txtfile: " + line)
            allUsers.add(line)
