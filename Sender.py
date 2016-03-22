
import socket

class Sender:
	"""classe responsavel pelo envio de requisições"""

	def __init__(this, address = "127.0.0.1", port = 6789):

		this.connection = (address, port)

		this.mySocket = socket.socket(socket.AF_INET,
		                         socket.SOCK_DGRAM,
		                         socket.IPPROTO_UDP)
		this.mySocket.setsockopt(socket.IPPROTO_IP,
		                         socket.IP_MULTICAST_TTL, 2)

	def run(this):
		while(True):
			message = input("insert message to send: ")
			this.mySocket.sendto(bytes(message, "utf-8", this.connection))
			if(message.upper() == 'EXIT'):break

