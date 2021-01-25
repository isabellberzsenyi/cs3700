import socket, sys

HOST = 'simple-service.ccs.neu.edu'
PORT = 27995
HELLO = "cs3700spring2021 HELLO 001274925\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((HOST, PORT))
except:
  sys.exit()

s.send(HELLO)

l = 1
while 1: 
  #receive FIND or BYE response
  resp = ''
  while 1:
    resp += s.recv(4096)
    if resp.endswith("\n"):
      break
  response_split = resp.split(" ")   

  if response_split[1] == 'FIND':
    find_symbol = response_split[2]
    resp_str = response_split[3]
  
    count = 0
    for i in resp_str:
      if i == find_symbol:
        count += 1

    s.send("cs3700spring2021 COUNT {}\n".format(count))
  else:
    print(response_split[2])
    break
s.close()
