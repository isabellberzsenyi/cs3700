import sys
import socket
from urllib.parse import urlparse

def POST():
  return 1

def GET(url):
  parsed_url = urlparse(url)

  # Should probably parse this into some useable object?? 
  # Or leave it as text idk - I'd want a library to pull the relevant info for me

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(30)
  
  try:
    s.connect((parsed_url.hostname, 80))
  except (ValueError, KeyError, TypeError) as e:
    print(e)
    sys.exit()

  data = f"GET {parsed_url.path} HTTP/1.0\r\nHOST: {parsed_url.hostname}\n\n"
  
  s.send(data.encode('utf-8'))

  try:
    response = ""
    while True:
      response += s.recv(8192).decode('utf-8')
      if '</html>' in response:
        break
    print(response)

  # check the response
  # pull of cookies
  # probably parse things into header, body, etc?

  except socket.error as e:
    print(e)
  return 1