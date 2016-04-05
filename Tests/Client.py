import socket
import threading

class Client(threading.Thread):

	def __init__(self, host = '127.0.0.1', port = 9999, size = 1024):
		threading.Thread.__init__(self)

		self.host = host
		self.port = port
		self.size = size

		self.tcp = socket.socket(socket.AF_INET,
		                         socket.SOCK_STREAM)
		self.tcp.connect((self.host, self.port))

	def run(self):

		while True:
			msg = input('digit exit to...')
			if msg is not 'exit':
				self.tcp.send(msg.encode('utf-8'))
			else:
				self.close()
				exit()