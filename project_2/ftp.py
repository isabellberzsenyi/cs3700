import socket, sys, re
OPERATION = sys.argv[1]
ARG1 = sys.argv[2].split('//')[1]
parse_args = ARG1.split('@')
#print(parse_args)

if (len(sys.argv) == 4):
  ARG2 = sys.argv[3]

USER = parse_args[0].split(':')[0]
#print('user', USER)
if len(parse_args[0].split(':')) == 2:
  PASSWORD = parse_args[0].split(':')[1]
 # print('pass', PASSWORD)
split_host = parse_args[1].split(':')
if len(split_host) == 1:
  # no port
  HOST = split_host[0].split('/', 1)[0]
  #print('host', HOST)

  if len(split_host[0].split('/', 1)) == 2:
    PATH = split_host[0].split('/', 1)[1]
    print('path', PATH)
elif len(split_host) == 2:
  # given port
  HOST = split_host[0]
  PORT = split_host[1].split('/', 1)[0]
  PATH = split_host[1].split('/', 1)[1]
  #print('host, port + path', HOST, PORT, PATH)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((HOST, 21))
  print("CONNECTED")
except:
  print('UH OH')
  sys.exit()

s.send('USER {}\r\n'.format(USER))
response = s.recv(8192)
print(response)
s.send('PASS ' + PASSWORD + '\r\n')
response = s.recv(8192)
print(response)

print('set type')
s.send('TYPE I\r\n')
response = s.recv(8192)
print(response)

print('set mode')
s.send('MODE S\r\n')
response = s.recv(8192)
print(response)

print('set stru')
s.send('STRU F\r\n')
response = s.recv(8192)
print(response)

if OPERATION == 'mkdir':
  print('mkdir')
  s.send('MKD ' + PATH + '\r\n')
  response = s.recv(8192)
  print(response)
elif OPERATION == 'rmdir':
  print('rmdir')
  s.send('RMD ' + PATH + '\r\n')
  response = s.recv(8192)
  print(response)
else:
  print('opening a channel')
  s.send('PASV\r\n')
  response = s.recv(8192)
  print(response)

  IP_PORT = re.split('[()]', response)[1]
  IP = reduce(lambda a, b: a + '.' + b,IP_PORT.split(',')[0:4])
  PORT2 = (int(IP_PORT.split(',')[4:][0]) << 8) + int(IP_PORT.split(',')[4:][1])
  print('opening data channel')
  data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    data.connect((IP, PORT2))
    print("data channel connected")
  except:
    print('Error connecting to data channel')
    sys.exit()
  if OPERATION == 'ls':
    print('list')
    s.send('LIST ' + PATH + '\r\n')
    response = s.recv(8192)
    print(response)
    response = data.recv(8192)
    print(response)
    response = s.recv(8192)
    print(response)
print('quit')
s.send('QUIT\r\n')
response = s.recv(8192)
print(response)
