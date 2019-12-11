#!/anaconda3/bin/python
# -*- coding: UTF-8 -*-
print ('Content-Type: text/html')
print ('')
import cgi,os
import socket,pickle
from socket import AF_INET, SOCK_DGRAM
import matplotlib.image as mpimg
from PIL import Image
import base64
from signal import signal, SIGPIPE, SIG_DFL, SIG_IGN
import cgitb;cgitb.enable()
signal(SIGPIPE, SIG_IGN)
form=cgi.FieldStorage()
fileitem=form['filename']
if fileitem.filename:
    fn=os.path.basename(fileitem.filename)
    open('/Users/chuci/apa/CGI-Executables/files/'+fn,'wb').write(fileitem.file.read())
    #message = mpimg.imread('/Users/chuci/apa/CGI-Executables/files/'+fn)
    #im = Image.open('/Users/chuci/apa/CGI-Executables/files/'+fn)
    #im1 = im.convert('L')
    #im1.save('/Users/chuci/apa/CGI-Executables/files/test123.png')
    #message = mpimg.imread('/Users/chuci/apa/CGI-Executables/files/test123.png')
    with open('/Users/chuci/apa/CGI-Executables/files/'+fn, "rb") as imageFile:
        message = base64.b64encode(imageFile.read())
    size = len(message)
#connection part
###############
    s = socket.socket()
    s.connect(('Chus-MacBook-Pro.local',1211))
    #s.settimeout(3)
    s.send(str(size).encode())
    data = s.recv(1024).decode()
    if data == 'yes':
        s.sendall(message)
        message = s.recv(1024).decode()
    else:
        message = 'error'
    '''
    while(True):
        try:
            s.send(str(size).encode())
            data = s.recv(1024).decode()
            if data == 'yes':
                s.send(message.encode())

            #message = repr(pickle.loads(data))
            #print('Received result', repr(pickle.loads(data)))
            s.close()
            break
        except :
            print ('Retrying after TimeoutError')
            continue
    '''

############## connnection part ends
    print ("""\
    <html>
    <head>
    <meta charset="utf-8">
    <title>CS655 geni project</title>
    </head>
    <body>
    <h1>Recognition complete!</h1>
    <p>The picture that you upload is:</p>
    <img src="/CGI-Executables/files/test123.png"  alt="upload picture" />
    <h2>The result is:{}</h2>
    <h2>size:{}</h2>
    <a href="/index1.html">
        <button>try again!</button>
    </a>
    </body>
    </html>
    """.format(message,size))
else:
    message='fail'
    print ("""\
    <html>
    <head>
    <meta charset="utf-8">
    <title>CS655 geni project</title>
    </head>
    <body>
    <h1>You don't upload the picture</h1>
    <a href="/index1.html">
        <button>try again!</button>
    </a>
    </body>
    </html>
    """)

