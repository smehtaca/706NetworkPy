import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 40020

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # INTERNET, UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	print "Recieved msg: ", data
