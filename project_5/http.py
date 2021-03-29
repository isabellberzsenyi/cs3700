import sys
import socket
from urllib.parse import urlparse
from html.parser import HTMLParser

def connect_socket(hostname):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(30)
  
  try:
    s.connect((hostname, 80))
    return s
  except (ValueError, KeyError, TypeError) as e:
    print(e)
    return -1
  

def check_response_status(response_status):
  if response_status == '200':
      print("OK")
      return 1
  elif response_status == '302':
    print('FOUND')
    return 1
  elif response_status == '301':
    print('MOVED')
    return -1
  elif (response_status == '403') or (response_status == '404'):
    print('NOT FOUND')
    return -1
  elif response_status == '500':
    print('ERROR')
    return -1

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
  def __init(self):
    super().__init__
    self.csrf_token = ''
    self.reset()
  def handle_starttag(self, tag, attrs):
    # find cookies in input tag
    if tag == "input":
      if ('name', 'csrfmiddlewaretoken') in attrs:
        for x, y in attrs:
          if x == 'value':
            self.csrf_token = y

def POST(url, tokens, body):
  parsed_url = urlparse(url)
  s = connect_socket(parsed_url.hostname)
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
    
    # tokens = getCookies(response)
  except socket.error as e:
    print(e)

  s.close()
  response_status = response.split("\n")[0].split(" ")[1]
  if check_response_status(response_status):
    tokens = getCookies(response)
    
    return tokens
  else:
    return -1


def GET(url, tokens = ""):
  parsed_url = urlparse(url)

  # Should probably parse this into some useable object?? 
  # Or leave it as text idk - I'd want a library to pull the relevant info for me
  s = connect_socket(parsed_url.hostname)
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
  # check the response
  response_status = response.split("\n")[0].split(" ")[1]
  if check_response_status(response_status):
    tokens = getCookies(response)
    # pull out csrfmiddlewaretoken
    if parsed_url.path == '/accounts/login/':
      p = TokenParse()
      p.feed(response)
      tokens['csrfmiddlewaretoken'] = p.csrf_token
    return tokens
  else:
    return -1

  