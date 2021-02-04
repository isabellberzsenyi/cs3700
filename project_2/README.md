## HIGH-LEVEL APPROACH

My high-level approach to solving the project was to overall follow the order given on the assignment sheet.

- First I created the necessary files and worked on parsing arguments for the 3700ftp shell script
- Parse the given url into: USER, PASS, HOST, PORT, PATH
- Connect to the TCP control channel by using the given username, password, host and port
  - Specifically send USER, PASS, TYPE, MODE, STRU, QUIT
- Implemented making and removing directories
- Implement creation of data channel
- Implement listing directory function
- Understand the actions involved for copy and move commands, and implement
- Testing, code clean up and refactoring

## CHALLENGES

The first challenge I was ran into was parsing the given url. The setup of the parameters, and the fact that some of them were optional was confusing to wrap my head around. I first attempted to use regex splitting, but this deemed to be a bit too complicated. Next, I decided to split the given url into from the '@': to get the USER[:PASSWORD] and HOST[:POST]/PATH. Then I split the USER and PASSWORD by ':', and the HOST[:POST]/PATH by ':'. If a PORT is provided then the length of the array is 2 and the PATH can be split from the PORT by '/', else the PATH can be split from the HOST similarly.

Another challenge I ran into was the concept of the 'cp' and 'mv' commands. I understand the usage and how it works within linux environment, but I did not understand the implementation when RETR and STOR both take a single path to file on the FTP Server. After doing some reading, and trial and error, I found out that the command for RETR and STOR should be sent to the control channel. Next, either the contents will be received from the server through the data channel or the contents from the local file are sent to the data channel.

## TESTING

To test the program I first tested the URL parsing through the following test cases:
Testing the FTP_URL in the following formats:

- all the params
  - ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
- no password
  - ftp://[USER@]HOST[:PORT]/PATH
- no username, default is "anonymous", default password is ""
  - ftp://[[:PASSWORD]@]HOST[:PORT]/PATH
- no username, no password
  - ftp://HOST[:PORT]/PATH
- no username, no password, no port
  - ftp://HOST/PATH
- no port, default is 21
  - ftp://[USER[:PASSWORD]@]HOST/PATH

Next, I tested all the commands to ensure that they work:

- ./3700ftp ls FTP_URL
- ./3700ftp mkdir FTP_URL
- ./3700ftp rmdir FTP_URL
- ./3700ftp rm FTP_URL
- ./3700ftp cp LOCAL_PATH FTP_URL
- ./3700ftp cp FTP_URL LOCAL_PATH
- ./3700ftp mv LOCAL_PATH FTP_URL
- ./3700ftp mv FTP_URL LOCAL_PATH
