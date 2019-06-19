import socket
import time
import threading


ip = "127.0.0.1"
PORT = 771
sockrecv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socksend = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sockrecv.bind(("127.0.0.1",770))


'''
def readfromfile():
    name_file = open("list.py","r")
    names = []
    for i in name_file.readlines():
        names = names.append[i]

    for i in names:
        names.split
        '''

def send():
    while True:
        body = raw_input("Pavan "+timestamp()+" : ")
        head = "\nPavan "+timestamp()+" : "
        if body.lower() is "quit":close()
        message = head+body
        socksend.sendto(message,(ip,PORT))

    return

def recive():
    while True:
         data = sockrecv.recv(10000)
         print(data)

    return


def close():
    sockrecv.close()
    socksend.close()
    return

def timestamp():
    return str(time.ctime())

try:

    threading.Thread(target=send,).start()
    threading.Thread(target=recive,).start()

except e as error:
    print(e)
    close()
