from socket import *
import os
from audioToMorse import morseAudioToText

class audioTCPclient:
    def __init__(self):
        pass

    def send(self, serverName='Chris', msg='morse.wav', serverPort=16000):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))  # establish the TCP connection
       
        clientSocket.send(msg.encode())  # send the audio message with send function (only in TCP)
        clientSocket.close()

    def receive(self, serverName='Chris', serverPort=16000):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))  # Establishing TCP connection

        morseMsg = clientSocket.recv(1024)  # Using the recv function (TCP only) to receive the data from the server
        recoveredMsg = morseAudioToText(morseMsg)  # implementing the morseAudioToText function which analyzes the wav
        # file and translates the morse code into alphanumeric

        for i in range(1, 100):
            if not os.path.exists('./recoveredFile.txt'):
                file2 = open(r"recoveredFile.txt", "w")
                file2.write(recoveredMsg)
                break
            elif not os.path.exists('./recoveredFile('+str(i)+').txt'):
                file2 = open('recoveredFile('+str(i)+').txt', "w")
                file2.write(recoveredMsg)
                break  # explained in audioUDPclient
        file2.close()
        clientSocket.close()  # closing the client socket

