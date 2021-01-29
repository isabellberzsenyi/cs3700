import socket, sys, re
OPERATION = sys.argv[1]
ARG1 = sys.argv[2]
ARG1 = ARG1.split('//')[1]
parse = re.split('[:@]', ARG1)

USER = parse[0]
if USER == '':
  USER = 'anonymous'
PASSWORD = parse[1]

split_hostname = parse[2].split('/', 1)
HOST = split_hostname[0].split(':')[0]
if len(split_hostname[0].split(':')) == 2:
  PORT = split_hostname[0].split(':')[1]
PATH = split_hostname[0]

if (len(sys.argv) == 4):
  ARG2 = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((HOST, 21))
  print("CONNECTED")
except:
  print('UH OH')
  sys.exit()
