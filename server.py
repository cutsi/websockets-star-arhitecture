import socket
import threading

DISCONNECT = "d"
HEADER = 1024
FORMAT = "utf-8"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(con, addr):
    print("[NEW CONNECTION FROM ] ", addr)
    connected = True
    while connected:
        msg = con.recv(HEADER).decode(FORMAT)
        if(msg):
            print ("address: ", addr, " | message: " + msg)
            if(msg == DISCONNECT):
                connected = False
        
    con.close()


def start():
    server.listen()
    print("SERVER LISTENING...")
    while True:
        clientsocket, address = server.accept()
        thread = threading.Thread(target=handle_client, args = (clientsocket,address))
        thread.start()
        print("[ACTIVE CONNECTIONS: ] ",  threading.activeCount() -1 )
        

start()


"""
while True:
    clientsocket, address = s.accept()
    msg = input("uneste rijec")
    print(f"connection from {address} have been established")
    clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.close()
    clientsocket.send(bytes("Welcome to the server"), FORMAT)"""