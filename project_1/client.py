import socket, sys

HOST = 'simple-service.ccs.neu.edu'
PORT = 27995
HELLO = "cs3700spring2021 HELLO 001274925"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('1')
try:
  s.connect((HOST, PORT))
except:
  print('BAD')
  sys.exit()

print('Connected')

s.send(HELLO)
data = s.recv(8192)
print(data)
