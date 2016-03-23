import socket
import struct


class Receiver:
    """classe responsavel pelo recebimento de requisiçoes"""

    def __init__(this, port=6789, address="224.225.226.227", buffersize=1024):
        this.buffersize = buffersize
        this.address = address
        this.port = port
        this.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM,
                                  socket.IPPROTO_UDP)
        this.sock.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR, 1)
        this.sock.bind('', this.port)

        this.mreq = struct.pack("=4sl",
                                socket.inet_aton(this.address),
                                socket.INADDR_ANY)

        this.sock.setsockopt(socket.IPPROTO_IP,
                             socket.IP_ADD_MEMBERSHIP, this.mreq)

    def run(this):
        while (True):
            print(this.sock.recv(this.buffersize))

receiver = Receiver()
