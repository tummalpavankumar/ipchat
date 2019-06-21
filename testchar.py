import socket
import time
import threading
import sqllite3 as sql

ping_data = "PING\r\n"

Naveen_ip = "192.168.10.100"
Ramesh_ip = "192.168.10.163"

PORT = 456

USERNAME = raw_input("Enter your user name: ")

nameserver = {}

db = sql.connect("namelsit.db")
db_cursor = db.cursor()

try:
	data_in_db = db_cursor.execute("SELECT * FROM namelist")
	
except error:
	db_cursor.execute("CREATE TABLE namelist('name','address')")
	data_in_db = db_cursor.execute("SELECT * FROM namelist")

name_dict = db_to_dict(data_in_db)

if USERNAME in name_dict:
	if (name_dict[USERNAME] is str(socket.gethostbyname(socket.gethostname()))):
		continue
	else:
		print("Username doesn't match with the ip address")
		closeall()
		exit()
ip = socket.gethostbyname(socket.gethostname())
#print ip
ping_data = "PING ON\r\n"
sockrecv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socksend = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sockrecv.bind((ip,PORT))


def db_to_dict(data_in_db):#converting database tuples into dictonary
	name_dict = {}
	for i in data_in_db:
		name_dict[str(i[0])] = str(i[1])
		
	return name_dict

def dict_to_db(name_dict): #converting dictonary into data a list of tuples
	for i in name_dict:
		db_cursor.execute("INSERT INTO namelist ('name','address') VALUES('"+str(i)+"','"+str(name_dict[i])+"')")	
	return

def updateusernames():


def send(): #sending message
    while True:
        body = raw_input("Pavan "+timestamp()+" : ")
        head = "\nPavan "+timestamp()+" : "
        if body.lower() is "quit":closeall()
        message = str(head+body)
        socksend.sendto(message,(Ramesh_ip,PORT))

    return

def recive(): #reciving message
    while True:
         data = sockrecv.recv(4096)
         if ("PING" in data):
			pinglive()
         print(data)

    return

def sendtoall(message):#to broad cast a message.
	for i in name_dict:
		socksend.sendto(message,(tuple(name_dict[i]),tuple(int(PORT))))
	return
	
def closeall(): #close all the open files, dbs , sockets.
    sockrecv.close()
    socksend.close()
	db_cursor.close()
	db.close()
    return

def timestamp(): #to create a time stamp i.e time and date
    return str(time.ctime())


def pinglive():
		while True:
			socksend.sendtoall("PING"+str(tuple(USERNAME)+tuple(int(PORT))))
			time.sleep(5)
		return

"""def ping():
    while True:
        socksend.sendtoall("PING "+str(tuple(USERNAME,IP)))
        time.sleep(5)
    return"""

try:

    threading.Thread(target=send,).start()
    threading.Thread(target=recive,).start()
	threading.Thread(target=pingtoall,).start()

except e as error:
    print(e)
    closeall()