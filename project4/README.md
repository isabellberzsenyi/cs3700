# High Level Approach

We implemented a pared down version of TCP using cumulative acks (by filtering the list of last sent messages to remove all messages with sequence numbers less than the last ack received), and retransmitting on 3 duplicate acks and timeouts.

We also implemented a sliding window of size 5000, and limited data sizes to 500 bytes (JSON encoding, in our experience, more than doubled the size of data we were attempting to encode) in order to ensure that the final packet size is < 1500 bytes.

## Testing approach

We tested using the provided test harness 'testall', as well as running individual tests using 'nettest' and a properly configured 'netsim'
