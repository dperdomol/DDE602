# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:36:29 2022

@author: diego
"""

#-Import necessary libraries 

#--import socket programming library
import socket, threading, textblob

def spellChecker(msg):
    arrWords = msg.split()
    for word in arrWords:
        word.lower()
        print("Word no spelling correction: ", word)
        # w = textblob.TextBlob(word)
        w = textblob.TextBlob(word)
        w2 = w.correct()
        if w != w2:
            print('Original Word {} - Suggested Word: {}'.format(w, w2))

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)
    def run(self):
        print("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ""
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            spellChecker(msg)
            if msg=='bye':
              break
            #print ("from client", msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()