import socket
FORMAT = "utf-8"
DISCONNECT = "disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = SERVER, PORT

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ADDR))
msg = DISCONNECT
while (msg):
    msg = input("unesite poruku: ")
    s.send(bytes(msg, FORMAT))
#print(msg.decode("utf-8"))

