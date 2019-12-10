import socketserver, pickle, socket    
from sklearn.decomposition import *
from skimage.transform import resize
from sklearn.preprocessing import scale
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
class MySockServer(socketserver.BaseRequestHandler):
   def handle(self):
      print ('Got a new connection from', self.client_address)
      while True:
         data = self.request.recv(1024)    
         if not data:
            break
         img = pickle.loads(data)
         print ('recv:', img)
         #ml
         digits = datasets.load_digits()
         data = scale(digits.data)
         X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, digits.target, digits.images, test_size=0.01, random_state=42)

         # Create the main SVC model for image recognition
         svc_model = svm.SVC(gamma=0.001, C=10, kernel='rbf')
         svc_model.fit(X_train, y_train)
         prediction = svc_model.predict([img])
         print('pre:',prediction)

         #process data here
         res = prediction[0]
         #time.sleep(4)
         resToClient = pickle.dumps(res)
         self.request.send(resToClient)
         print ('sent', res)

if __name__ == '__main__':    
     HOST = socket.gethostname()
     print(HOST)           
     PORT = 1133
     print(PORT)         
     s = socketserver.ThreadingTCPServer((HOST, PORT), MySockServer)
     print ("socket is listening") 
     s.serve_forever()