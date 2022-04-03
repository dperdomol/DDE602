# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:36:29 2022

@author: diego
"""

#-Import necessary libraries 

#--import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

#Thread function
def threaded(c):
    while True:
        
        #Data received from client
        data = c.recv(1024)
        if not data:
            print('bye')
            
            #Lock released on exit
            print_lock.release()
            break
        
        #reverse the given string from client
        data = data[::-1]
        
        #send back reversed string to client
        c.send(data)
        
    #Connection closed
    c.close()
    
def Main():
    host = ""
    #Reserve a port on your computer
    #In this case is 8808
    port = 8808
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket binded to port", port)
    
    #put the socket into listening mode
    s.listen(5)
    print("Socket is listening")
    
    #A forever loop until client wants to exit
    while True:
        
        #Establish connection with client
        c, addr = s.accept()
        
        #Lock acquired by client
        print_lock.acquire()
        print("Connected to :", addr[0] , ":", addr[1])
    
        #Start a new thread and return its indentifier
        start_new_thread(threaded, (c,))
    s.close()
    
if __name__ == '__main__':
    Main()