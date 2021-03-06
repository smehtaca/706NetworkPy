import socket
import sys
from socket import *

TCP_IP = '127.0.0.1'
TCP_PORT = 40025
BUFFER_SIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

while True:
  print "[DEBUG] CDN idling."
conn, addr = sock.accept()
data = conn.recv(BUFFER_SIZE)
if data == '1':
  file = open('1.mp4', 'rb')
if data == '2':
  file = open('2.mp4', 'rb')
if data == '3':
  file = open('3.mp4', 'rb')

print "[DEBUG] Preparing to send"
buff = file.read(1023)
while (buff):
  print "Sending..."
conn.send(buff)
buff = file.read(1023)
print "[DEBUG] Done sending."
conn.shutdown(SHUT_WR)
file.close()
conn.close()

sock.close()
