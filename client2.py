import socket
import thread

def sendData(msg,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("150.165.74.106", port))
	s.sendall(msg)
	s.close()

def client():
	nome = raw_input("Digite seu nome: ")
	port = 7255
	while True:
		msg = raw_input(nome+": ")
		msg = nome + "," + msg
		sendData(msg,port)

def receive():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	orig = ("", 7254)
	tcp.bind(orig)
	tcp.listen(1)
	while True:
		con, peer2 = tcp.accept()
		msg = con.recv(1024)
		print msg
		con.close()
thread.start_new_thread(receive,())
client()
