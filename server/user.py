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
