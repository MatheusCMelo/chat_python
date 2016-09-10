import socket
import thread
def sendData(msg,host,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.sendall(msg)
	s.close()
def server(con,cliente):
	cliente = cliente[0]
	msg = con.recv(1024)
	if cliente not in clientes:
		clientes.append(cliente)
	for i in clientes:
		if i != cliente:
			clientes2.append(i)
	msg = msg.split(",")
	print clientes2
	for i in clientes2:
		sendData(msg[0]+": "+msg[1],i,7254)
	thread.exit()
clientes = []
clientes2 = []
HOST = ''
PORT = 7255
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(2)
while True:
	con, cliente = tcp.accept()
	thread.start_new_thread(server,(con,cliente))
	clientes2 = []
