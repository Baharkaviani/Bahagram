"""
Created on Mon Nov 30 18:50:00 2020 (1399/9/10)
@author: Bahar Kaviani
description: Global information about all users
"""
import socket
import threading
import user as user

### global variables
# list of all connected IPs with their usernames
allUsers = []

"""
Defined on Thu Dec 3 18:06:00 2020 (1399/9/13)
description: add all users from users.txt to allUsers set
"""
def initializeAllUsers():
    # Reading from file and then close the file
    with open("users.txt", "r") as usersFile:
        for line in usersFile:
            # extra print for checking
            print("[users.txtfile]: " + line)

            IP, username = line.split(":")
            x = user.User(IP, username)
            allUsers.append(x)