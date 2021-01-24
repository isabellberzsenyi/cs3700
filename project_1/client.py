import socket, sys

HOST = 'simple-service.css.neu.edu'
PORT = 27995

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('1')
try:
  s.connect((HOST, PORT))
except:
  print('BAD')
  sys.exit()

print('Connected')
