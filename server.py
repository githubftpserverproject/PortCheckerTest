import socket

open_port = int(input("port:"))
sockets = []

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',open_port))

sock.listen(5)

c,addr = sock.accept()

print("Connection from "+str(addr))
sock.close()
