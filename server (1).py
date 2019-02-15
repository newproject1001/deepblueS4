import socket
import sys
import csv
import datetime as d


csvFile=open('data.csv', 'a')
row = ['date','time','Location','Light_Problem','Water_Isuue','Dirty_Smells']
writer = csv.writer(csvFile)
writer.writerow(row)

csvFile.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(100)



lc=1
wc=1
gc=1

    
while True:
    
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    data = connection.recv(1024)
    i=data
    if i=='clean toilet':
        csvFile=open('data.csv', 'a')
        ct=str(d.datetime.now())
        l=ct.split()
        l.append(client_address)
        l.append('null')
        l.append('null')
        l.append(gc)
        gc=gc+1
        writer = csv.writer(csvFile)
        writer.writerow(l)



    if i=='light issue':
        csvFile=open('data.csv', 'a')
        ct=str(d.datetime.now())
        l=ct.split()
        l.append(client_address)
        l.append(lc)
        l.append('null')
        l.append('null')
        lc=lc+1
        writer = csv.writer(csvFile)
        writer.writerow(l)
        


    if i=='water over':
        csvFile=open('data.csv', 'a')
        ct=str(d.datetime.now())
        l=ct.split()
        l.append(client_address)
        l.append('null')
        l.append(wc)
        l.append('null')
        wc=wc+1
        writer = csv.writer(csvFile)
        writer.writerow(l)

    
    print('received ',i)
    connection.send(str(i).encode('utf-8'))

