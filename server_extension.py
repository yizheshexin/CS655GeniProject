##import socket, pickle
##import time              
##  
### next create a socket object 
##s = socket.socket()  
##port = 1234    #need to modify
##s.bind(('', port))     
##s.listen(5)      
##print ("socket is listening")         
##while True: 
##   # Establish connection with client. 
##   conn, addr = s.accept()      
##   print ('Got connection from', addr )
##   #data from client
##   data = conn.recv(1024)
##   #process data
##   resToClient = pickle.dumps(1)
##   #time.sleep(4)
##   conn.send(resToClient) 
##   print(pickle.loads(data))
##   # Close the connection with the client 
##   conn.close()   
##

import socketserver, pickle, socket
import base64         
from imageai.Prediction import ImagePrediction
import os
from model import prediction
class MySockServer(socketserver.BaseRequestHandler):
    def handle(self):
        print ('Got a new connection from', self.client_address)
       #while True:
        data = self.request.recv(1024)    
        #toBack = pickle.loads(data)
        #print ('recv:', toBack)
        print ('recv:', data.decode())
        self.request.send('yes'.encode())
        size = int(data.decode())
        print('size',size)
        image = ''
        lastsize = -1
        while len(image)< size:
          #if lastsize == len(image):
          #    break
           newdata = self.request.recv(1024*500).decode()
           image += str(newdata)
           #print(lastsize)
           print(len(image))
           #lastsize = len(image)
        #print(image)
        fh = open("/Users/chuci/Desktop/cs655/geni-project/imageToSave.png", "wb")
        fh.write(base64.decodestring(image.encode()))
        fh.close()

        #ml:
        predictions, percentage_probabilities = prediction.predictImage("/Users/chuci/Desktop/cs655/geni-project/imageToSave.png", result_count=5)
        for index in range(len(predictions)):
            print(str(predictions[index]) + " : " + str(percentage_probabilities[index]))
        self.request.send(str(len(image)).encode())
        print ('sent1234')

if __name__ == '__main__':    
     HOST = socket.gethostname() # get hostname''
     print('host:',HOST)             
     PORT = 1211          
     s = socketserver.ThreadingTCPServer((HOST, PORT), MySockServer)
     print ("socket is listening") 
     s.serve_forever()     
