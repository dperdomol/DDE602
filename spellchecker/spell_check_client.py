import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("out_data",'UTF-8'))

def breakTheFile(fileName):
    
    count = 0
    ArrWords = []
    
    with open(fileName) as file:
    
        for line in file:
            count += 1
            wordList = line.split()
            for word in wordList:
                word.lower()
                ArrWords.append(word)
               
    return ArrWords
    # for word in ArrWords:
    #     print(word)

while True:
    
    test = breakTheFile('textForTest.txt')
    
    in_data =  client.recv(1024)
    print("From Server :" ,in_data.decode())
    out_data = input()
    client.sendall(bytes(test,'UTF-8'))
    if out_data=='bye':
        break
client.close()