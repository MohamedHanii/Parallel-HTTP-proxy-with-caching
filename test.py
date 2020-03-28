import socket


#SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1",12356))

s.listen(5)

while True:
    C_Socket,Addr = s.accept()
    C_Socket.send(b'Hello')


#CLIENT
