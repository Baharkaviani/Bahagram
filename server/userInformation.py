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
    # read from file and then close the file
    with open("users.txt", "r") as usersFile:
        for line in usersFile:
            # # extra print for checking
            # print("[users.txtfile]: " + line)
            IP, username = line.split(":")
            x = user.User(IP, username)
            allUsers.append(x)

"""
Defined on Fri Dec 4 11:56:00 2020 (1399/9/14)
description: add new user to allUsers set
"""
def addUser(IP, username):
    x = user.User(IP, username)

    with open("users.txt", "a") as usersFile:
        usersFile.write(x.IP + ":" + x.username)
        usersFile.write("\n")

    allUsers.append(x)
