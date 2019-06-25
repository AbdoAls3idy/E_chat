import socket
import time
import threading
import pickle
import sys
from PyQt5.QtCore import QThread
from Cryptodome.Cipher import AES
from Cryptodome import Random
import base64
import bitstring
class Client(QThread):
    global key
    #global iv
    key = b'a2s3d4f5g8q9w8r2'
    #key = base64.b64encode(key)

    iv = Random.new().read(AES.block_size)
    global encrypt
    global decrypt

    def __init__(self, host, port, sendBtn, nickname, messageEdit, receivedMessage):
        super(Client, self).__init__(parent = None)
        # set local variables to the provided arguments
        self.receivedMessage = receivedMessage
        self.nickname = nickname        # used for identification by server and other clients
        self.port = port                # the port used to connect to the server
        self.host = host                # the hostname used to connect to the server
        self.messageEdit = messageEdit  # instance of the field where text to be sent is typed, it is
                                        #   needed to detect if user presses return to send message

        # initialize variable to an empty string
        self.message = ""

        # flag that indicates if client is running
        self.running = True

        # connect the "self.send" slot to its signals 
        # on clicking send button the send method is called
        sendBtn.clicked.connect(self.send)
        # send method is called on hitting return in the message edit field
        self.messageEdit.returnPressed.connect(self.send)

        # create an instance of socket
        self.clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to server
        # try except block because we may try to connect to a server that may not be running
        try:
            self.clientsoc.connect((self.host, self.port))
            self.clientsoc.send(pickle.dumps(self.nickname))
            self.receivedMessage.append("Connected to server")
        except:
            print("Could not connect to server")        # print error
            self.stop()         # call method to close connection with the server
            sys.exit()          # stop the script

    def encrypt(self, msg):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        self.msg = msg
        msg = cipher.encrypt(msg)
        data = [msg ,iv]
        return data

    def decrypt(self, data):  # Not Fucking work
        iv = data[1]
        chiper_plain = AES.new(key, AES.MODE_CFB, iv)
        self.msg = data[0]
        de_msg = chiper_plain.decrypt(self.msg)
        return (de_msg)

    # This method will be threaded by QThread when the inherited method start is called
    def run(self):
        while self.running:
            self.receive()      # call the receive method

    # method to receive messages forwarded byt he server
    def receive(self):
        while self.running:
            # try except block to handle situations where server suddenly stops running 
            # and client is still running
            try:
                # receive message in byte format from server 
                self.data = self.clientsoc.recv(1024)
                self.data = pickle.loads(self.data) #22222   # convert from yte format to python list
                #print(b"receved data" + self.data)
                self.data = decrypt(self, self.data)
                self.data = pickle.loads(self.data)
                print(self.data)



                #self.data = pickle.loads(self.data) #555555
                #self.data = bytes.fromhex(self.data) #5555555
                # if data is not none
                if self.data:        
                    # print the nickname and the message        
                    print(str(self.data[0] + ": " +self.data[1]))    # first index is the senders nickname, second index is the message
                    # do not show the message if you're the sender
                    if self.data[0] != self.nickname:
                        #self.emit(QtCore.SIGNAL("MESSAGES", self.message))
                        self.receivedMessage.append(str(self.data[0] + ": " +self.data[1]))
            except:
                # To Do make pop up to show error
                print("Error receiving")       # print error
                self.stop()                    # call method to close connection with the server
                sys.exit()                     # stop the program

    # method to send message currently in the message edit field to the server
    # this method is a PyQt slot
    def send(self):
        self.message = self.messageEdit.text()                  # get the text currently in the text edit field
        self.receivedMessage.append("You: " + self.message)     # show the message in chat history
        self.messageEdit.setText("")                            # set the text in the text edit field to an empty string
        self.data = (self.nickname, self.message)               # bundle up senders nickname and the message into a list
        self.data = pickle.dumps(self.data)
        self.data = encrypt(self,self.data)
        self.data = pickle.dumps(self.data)                    # convert the list to byte format
        #self.data = bytes.hex(self.data) #555555555555
        #print(b"send data" + self.data)


        # try except block because server may not be running
        try:
            self.clientsoc.send(self.data)  # pickle.dumps       # send the message to the server
        except:
            print("Error sending message")

    # method to close connection with the server
    def stop(self):
        self.running = False        # set flag to false
        self.clientsoc.close()      # close the socket