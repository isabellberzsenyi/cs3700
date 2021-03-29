import sys
import socket


def POST():
  return 1

def GET(HOST, data):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(30)
  
  try:
    s.connect((HOST, 80))
  except (ValueError, KeyError, TypeError) as e:
    print(e)
    sys.exit()
  
  s.send(data.encode('utf-8'))

  try:
    response = ""
    while True:
      response += s.recv(8192).decode('utf-8')
      if '</html>' in response:
        break
    print(response)

  except socket.error as e:
    print(e)
  return 1