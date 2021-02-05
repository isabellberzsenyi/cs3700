import socket, sys, re, os

def check_response(resp):
  print(resp)
  if resp.find('1') == -1 and resp.find('2') == -1:
    print('Error occured!')
    sys.exit()

def main():
  OPERATION = sys.argv[1]
  if len(sys.argv) == 4:
    if sys.argv[2].find("ftp") == -1:
      ARG1 = sys.argv[3]
      ARG2 = sys.argv[2]
      DIRECTION = 'send'
    elif sys.argv[3].find("ftp") == -1:
      ARG1 = sys.argv[2]
      ARG2 = sys.argv[3]
      DIRECTION = 'retrieve'
    else:
      print('Incorrect ftp URL provided')
      sys.exit()
  else:
    ARG1 = sys.argv[2]

  ARG1 = ARG1.split('//')[1]
  parse_args = ARG1.split('@')

  # either username or password given
  if len(parse_args) == 2:
    # check if password is given
    if len(parse_args[0].split(':')) == 2:
      PASSWORD = parse_args[0].split(':')[1]
    else:
      PASSWORD = ""
  
    USER = parse_args[0].split(':')[0]
    if USER == "":
      # no username provided, go to default with password
      USER = "anonymous"
      PASSWORD = ""

    split_host = parse_args[1].split(':')
  else:
    USER = "anonymous"
    PASSWORD = ""
    split_host = ARG1.split(':')

  # check if port is given
  if len(split_host) == 1:
    # port is given
    HOST = split_host[0].split('/', 1)[0]
    PATH = split_host[0].split('/', 1)[1]
    PORT = 21
  elif len(split_host) == 2:
    HOST = split_host[0]
    PORT = int(split_host[1].split('/', 1)[0])
    PATH = split_host[1].split('/', 1)[1]

  # connect to control channel
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.connect((HOST, PORT))
  except:
    print('Error connecting to host socket')
    sys.exit()

  # send USER command
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
  
  # send PASS command
  if PASSWORD:
    s.send('PASS ' + PASSWORD + '\r\n')
    response = s.recv(8192)
    print(response)

  # send TYPE command
  s.send('TYPE I\r\n')
  check_response(s.recv(8192))

  # send MODE command
  s.send('MODE S\r\n')
  check_response(s.recv(8192))

  # send STRU command
  s.send('STRU F\r\n')
  check_response(s.recv(8192))

  # check operation
  if OPERATION == 'mkdir':
    s.send('MKD ' + PATH + '\r\n')
    check_response(s.recv(8192))
  elif OPERATION == 'rmdir':
    s.send('RMD ' + PATH + '\r\n')
    check_response(s.recv(8192))
  elif OPERATION == 'rm':
    s.send('DELE ' + PATH + '\r\n')
    check_response(s.recv(8192))
  else:
    # if ls, cp or mv
    s.send('PASV\r\n')
    response = s.recv(8192)
    check_response(response)

    IP_PORT = re.split('[()]', response)[1]
    IP = reduce(lambda a, b: a + '.' + b,IP_PORT.split(',')[0:4])
    PORT2 = (int(IP_PORT.split(',')[4:][0]) << 8) + int(IP_PORT.split(',')[4:][1])
    
    # open data channel
    data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      data.connect((IP, PORT2))
    except:
      print('Error connecting to data channel')
      sys.exit()
    if OPERATION == 'ls':
      s.send('LIST ' + PATH + '\r\n')
      check_response(s.recv(8192))
      response = data.recv(8192)
      print(response)
      check_response(s.recv(8192))
    elif OPERATION == 'cp' or OPERATION == 'mv':
      if DIRECTION == 'send':
        s.send('STOR ' + PATH + '\r\n')
        check_response(s.recv(8192))
        f = open(ARG2, "r")
        data.send(f.read())
        data.close()
        f.close()
        check_response(s.recv(8192))
        if OPERATION == 'mv':
          os.remove(ARG2)
      else:
        s.send('RETR ' + PATH + '\r\n')
        check_response(s.recv(8192))
        f = open(ARG2, "w")
        response = data.recv(8192)
        print(response)
        f.write(response)
        f.close()
        check_response(s.recv(8192))
        if OPERATION == 'mv':
          s.send('DELE ' + PATH + '\r\n')
          check_response(s.recv(8192))

  s.send('QUIT\r\n')
  check_response(s.recv(8192))
  s.close()

if __name__ == "__main__":
  main()
