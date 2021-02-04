import socket, sys, re, os
OPERATION = sys.argv[1]

if len(sys.argv) == 4:
  if sys.argv[2].find("ftp") == -1:
    ARG1 = sys.argv[3]
    ARG2 = sys.argv[2]
    DIRECTION = 'send'
  else:
    ARG1 = sys.argv[2]
    ARG2 = sys.argv[3]
    DIRECTION = 'retrieve'
else:
  ARG1 = sys.argv[2]

ARG1 = ARG1.split('//')[1]
parse_args = ARG1.split('@')

USER = parse_args[0].split(':')[0]
if len(parse_args[0].split(':')) == 2:
  PASSWORD = parse_args[0].split(':')[1]
else:
  PASSWORD = ""
split_host = parse_args[1].split(':')

if len(split_host) == 1:
  HOST = split_host[0].split('/', 1)[0]
  if len(split_host[0].split('/', 1)) == 2:
    PATH = split_host[0].split('/', 1)[1]
elif len(split_host) == 2:
  HOST = split_host[0]
  PORT = split_host[1].split('/', 1)[0]
  PATH = split_host[1].split('/', 1)[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((HOST, 21))
except:
  print('Error connecting to host socket')
  sys.exit()

s.send('USER {}\r\n'.format(USER))
while 1:
  response = s.recv(8192)
  print(response)
  if response.find('3') != -1:
    break
  elif response.find('5') != -1:
    print('Error loging in')
    sys.exit()
    break
if PASSWORD:
  s.send('PASS ' + PASSWORD + '\r\n')
  response = s.recv(8192)
  print(response)

s.send('TYPE I\r\n')
response = s.recv(8192)
print(response)

s.send('MODE S\r\n')
response = s.recv(8192)
print(response)

s.send('STRU F\r\n')
response = s.recv(8192)
print(response)

if OPERATION == 'mkdir':
  s.send('MKD ' + PATH + '\r\n')
  response = s.recv(8192)
  print(response)
elif OPERATION == 'rmdir':
  s.send('RMD ' + PATH + '\r\n')
  response = s.recv(8192)
  print(response)
elif OPERATION == 'rm':
  s.send('DELE ' + PATH + '\r\n')
  response = s.recv(8192)
  print(response)
else:
  s.send('PASV\r\n')
  response = s.recv(8192)
  print(response)

  IP_PORT = re.split('[()]', response)[1]
  IP = reduce(lambda a, b: a + '.' + b,IP_PORT.split(',')[0:4])
  PORT2 = (int(IP_PORT.split(',')[4:][0]) << 8) + int(IP_PORT.split(',')[4:][1])
  
  data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    data.connect((IP, PORT2))
  except:
    print('Error connecting to data channel')
    sys.exit()
  if OPERATION == 'ls':
    s.send('LIST ' + PATH + '\r\n')
    response = s.recv(8192)
    print(response)
    response = data.recv(8192)
    print(response)
    response = s.recv(8192)
    print(response)
  elif OPERATION == 'cp' or OPERATION == 'mv':
    if DIRECTION == 'send':
      s.send('STOR ' + PATH + '\r\n')
      response = s.recv(8192)
      print(response)
      if response.split(" ")[0] == "150":
        f = open(ARG2, "r")
        data.send(f.read())
        data.close()
        f.close()
        response = s.recv(8192)
        print(response)
        if OPERATION == 'mv':
          os.remove(ARG2)
    else:
      s.send('RETR ' + PATH + '\r\n')
      response = s.recv(8192)
      print(response)
      if response.split(" ")[0] == "150":
        f = open(ARG2, "w")
        response = data.recv(8192)
        print(response)
        f.write(response)
        f.close()
        response = s.recv(8192)
        print(response)
        if OPERATION == 'mv':
          s.send('DELE ' + PATH + '\r\n')
          response = s.recv(8192)
          print(response)
  """
  elif OPERATION == 'mv':
    if DIRECTION == 'send':
      s.send('STOR ' + PATH + '\r\n')
      response = s.recv(8192)
      print(response)
      if response.split(" ")[0] == "150":
        f = open(ARG2, "r")
        data.send(f.read())
        data.close()
        f.close()
        response = s.recv(8192)
        print(response)
        os.remove(ARG2)
    
    else:
      s.send('RETR ' + PATH + '\r\n')
      response = s.recv(8192)
      print(response)
      if response.split(" ")[0] == "150":
        f = open(ARG2, "w")
        response = data.recv(8192)
        print(response)
        f.write(response)
        f.close()
        response = s.recv(8192)
        print(response)
        s.send('DELE ' + PATH + '\r\n')
        response = s.recv(8192)
        print(response)
        """

s.send('QUIT\r\n')
response = s.recv(8192)
print(response)
s.close()
