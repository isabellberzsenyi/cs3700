import sys
import socket
from urllib.parse import urlparse
from html.parser import HTMLParser

def connectSocket(hostname):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(30)
  
  try:
    s.connect((hostname, 80))
    return s
  except (ValueError, KeyError, TypeError) as e:
    print(e)
    return -1

def getMiddlewareToken(response):
  p = TokenParse()
  p.feed(response)
  return p.csrf_middleware_token

def getCookies(response):
  tokens = {}
  if 'Set-Cookie' in response:
    split = response.split('\n')
    for x in split:
      if 'Set-Cookie' in x:
        if 'csrftoken' in x:
          tokens['csrftoken'] = x.split(";")[0].split('=')[1]
        elif 'sessionid' in x:
          tokens['sessionid'] = x.split(";")[0].split('=')[1]

  return tokens

class TokenParse(HTMLParser):
  def __init__(self):
    super().__init__()
    self.csrf_middleware_token = ''
    self.reset()
  def handle_starttag(self, tag, attrs):
    # find cookies in input tag
    if tag == "input": 
      if ('name', 'csrfmiddlewaretoken') in attrs:
        for x, y in attrs:
          if x == 'value':
            self.csrf_middleware_token = y


def POST(url, tokens, body):
  parsed_url = urlparse(url)
  s = connectSocket(parsed_url.hostname)
  if s == -1:
    sys.exit()
  
  data = f"POST {parsed_url.path} HTTP/1.0\r\n"
  data += f"Host: {parsed_url.hostname}\r\n"
  data += "Content-Type: application/x-www-form-urlencoded\r\n"
  data += "Content-Length: " + str(len(body)) + "\r\n"
  data += "Cookie: csrftoken="+tokens["csrftoken"]+"\r\n"
  data += "\r\n"
  data += body
  
  s.send(data.encode('utf-8'))
  
  try:
    response = ""
    while True:
      response = s.recv(8192).decode('utf-8')
      if '\r\n' in response:
        break
    
    
  except socket.error as e:
    print(e)

  s.close()
  return response

def GET(url, tokens = ""):
  parsed_url = urlparse(url)

  # Should probably parse this into some useable object?? 
  # Or leave it as text idk - I'd want a library to pull the relevant info for me
  s = connectSocket(parsed_url.hostname)
  if s == -1:
    sys.exit()

  data = f"GET {parsed_url.path} HTTP/1.0\r\nHost: {parsed_url.hostname}"
  if tokens:
    data += "\r\n"
    data += f"Cookie: csrftoken="+tokens["csrftoken"]+"; sessionid="+tokens["sessionid"]+";\n\n"
  else:
    data += "\n\n"
  
  s.send(data.encode('utf-8'))

  try:
    response = ""
    while True:
      received = s.recv(8192).decode('utf-8')
      response += received

      if '</html>' in response:
        break
    # probably parse things into header, body, etc?
    # parse csrftoken from response
  except socket.error as e:
    print(e)
  
  s.close()
  return response