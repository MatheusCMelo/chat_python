import socket
import thread
def sendData(msg,peer2):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((peer2, 5002))
	s.sendall(msg)
	s.close()
def client(peer2):
	print "oi"
	while True:
		msg = raw_input()
		sendData(msg,peer2)
def server():
	print "oi"
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	orig = ("", 5001)
	tcp.bind(orig)
	tcp.listen(1)
	while True:
		con, peer2 = tcp.accept()
		msg = con.recv(1024)
		print peer2, msg
		con.close()
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = ("", 5000)
tcp.bind(orig)
tcp.listen(1)
con, peer2 = tcp.accept()
peer2 = peer2[0]
con.close()
print peer2
thread.start_new_thread(server,())
client(peer2)
