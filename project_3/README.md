# Milestone 1 

## Milestone 1 Approach

We implemented two things for milestone 1: 
- We created the routing table as a list of ForwardingTableEntries, each of which contained a network, netmask, srcif (interface describing the socket). We then implemented an update function which, given an update message, will add an entry to our routing table.
- We implemented the forward and dump functions to pass on messages we received and print out the forwarding table


## Milestone 1 Testing
- We tested using the given milestone tests.