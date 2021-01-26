## HIGH-LEVEL APPROACH

My high-level approach to solve the problem was to:

- create a TCP socket
- send the HELLO message and print the FIND messages
- count the ASCII characer in a random string
- send COUNT message with the result, test that it works when another FIND message is received
- add a while loop until server receives a BYE message
- resolve not reading full message from server

## CHALLENGES

I found out that in my reading of the FIND messages from the server I was not reading in the full random string sent. I found this out because I was receiving a message that was not in the proper format. To fix this error, I created a while loop that read from the server until the string ended with a newline character. Lastly, I added a timeout so the loop is finite and an error is printed once timed out.

A challenge I was facing while working on creating an encrypted SSL socket, was receiving a "SSL Certificate Verify Failed" error. Looking into the error, I found out that I had to make a default context for the SSL. Then I had to set the set_hostname and verify_mode settings for the context. This solved the error of an improper SSL socket.

## TESTING

To test my code I tested all combinations of having 2 optional arguments (-p and -s) and 2 required arguments (hostname and neu id). Including:

- ./client -p PORT -s hostname neu_id
  Ensure that the port given overrides the default for SSL socket
- ./client -s hostname neu_id
  Ensure that the SSL socket is used, and proper secret_flag is returned
- ./client -p PORT hostname neu_id
  Ensure that the port given is used
- ./client hostname neu_id
  Ensure that the default port (27995) is used on TCP socket
