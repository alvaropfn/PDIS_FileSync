import socket
import threading

class Server(threading.Thread):

	def __init__(self, host = '', port = 9999, size = 1024):
		threading.Thread.__init__(self)

		self.host = host
		self.port = port
		self.size = size

		self.tcp = socket.socket(socket.AF_INET,
		                         socket.SOCK_STREAM)
		self.tcp.bind((self.host, self.port))
		self.tcp.listen(5)

	def connectWith(self, conn, client):
		print('connected with' + str(client))

		while True:
			msg = conn.recv(self.size)
			msg = msg.decode('utf-8')
			if not msg: break
			print(str(client) + ": " + str(msg))

		print('connection termineted with: ' + client)
		conn.close()
		exit()

	def run(self):

		while True:
			con, clt = self.tcp.accept()
			threading._start_new_thread(self.connectWith, (con, clt))
		self.tcp.close()

