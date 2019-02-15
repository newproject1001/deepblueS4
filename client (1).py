import socket
import sys
import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(7,g.IN)#gas sensor
g.setup(13,g.IN)#ldr sensor
g.setup(15,g.IN)#water sensor
g.setup(11,g.OUT)#gas light
g.setup(12,g.OUT)#light
g.setup(16,g.OUT)#water light
g.output(12,False)
g.output(11,False)
g.output(16,False)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
data='Chembur 1'
sock.send(data.encode('utf-8'))
connect =True

gc=0
lc=0
wc=0

while True:
        try :
                gn=g.input(7)
                ln=g.input(13)
                wn=g.input(15)
                print(gc,lc,wc)
                if gn==0 and gc<=20:
                    gc=gc+1
                if gn==1 and gc>0:
                    gc=gc-1

                if gc>20:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_address = ('localhost', 10000)
                    print (sys.stderr, 'connecting to %s port %s' % server_address)
                    sock.connect(server_address)
                    data='clean toilet'
                    sock.send(data.encode('utf-8'))
                    gc=11


                    
                if ln==0 and lc>0:
                    lc=lc-1
                if ln==1 and lc<=20:
                    lc=lc+1
                
                if lc>20:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_address = ('localhost', 10000)
                    print (sys.stderr, 'connecting to %s port %s' % server_address)
                    sock.connect(server_address)
                    data='light issue'
                    sock.send(data.encode('utf-8'))
                    lc=11

                    

                    
                if wn==0 and wc>0:
                    wc=wc-1
                if wn==1 and wc<=20:
                    wc=wc+1

                if wc>20:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_address = ('localhost', 10000)
                    print (sys.stderr, 'connecting to %s port %s' % server_address)
                    sock.connect(server_address)
                    data='water over'
                    sock.send(data.encode('utf-8'))
                    wc=11




                if gc>10:
                        g.output(11,True)          
                if lc>10:
                        g.output(12,True)
                if wc>10:
                        g.output(16,True)

                        
                if gc<10:
                        g.output(11,False)

                if lc<10:
                        g.output(12,False)
                        
                if wc<10: 
                        g.output(16,False)
                
                
		
                time.sleep(1)
        except socket.error:
                connect = False
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("connection lost re-connection")
                
                    
                while not connect:
                        try:
                                sock.connect(server_address)
                                data='Chembur 1'
                                sock.send(data.encode('utf-8'))
                                connect=True
                                print("re-connection successful")
                                
                        except socket.error:
                                time.sleep(5)
