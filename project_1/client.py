import socket, sys, ssl, time

PORT = int(sys.argv[1])
S_FLAG = int(sys.argv[2])
HOST = sys.argv[3]
ID = sys.argv[4]

HELLO = "cs3700spring2021 HELLO {}\n".format(ID)

if S_FLAG:
  context = ssl.create_default_context()
  context.check_hostname = False
  context.verify_mode = ssl.CERT_NONE

  sock = socket.create_connection((HOST, PORT))
  s = context.wrap_socket(sock, server_hostname=HOST)
else:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.connect((HOST, PORT))
  except:
    print("Error connecting")
    sys.exit()

# send HELLO messsge
s.send(HELLO)

while 1: 
  # receive FIND or BYE response
  response = ''
  timeout = time.time() + 60
  while 1:
    response += s.recv(8192)
    if response.endswith("\n"):
      break
    elif time.time() > timeout:
      print("Error reading from server")
      sys.exit()
      
  response_split = response.split(" ")   

  if (len(response_split) != 3) and (len(response_split) != 4):
    print("Error: Bad response 2")
    sys.exit()

  # deal with FIND response
  if response_split[1] == 'FIND':
    find_symbol = response_split[2]
    resp_str = response_split[3]
  
    count = 0
    for i in resp_str:
      if i == find_symbol:
        count += 1

    # send COUNT response
    s.send("cs3700spring2021 COUNT {}\n".format(count))
  elif response_split[1] == 'BYE':
    # print secret flagz
    print(response_split[2].rstrip())
    break
  else:
    print("Error: Bad response")
    sys.exit()

if S_FLAG:
  sock.close()
s.close()
