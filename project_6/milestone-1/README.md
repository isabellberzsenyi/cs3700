## High Level Approach
- Initially we started with responding to all client requests with a fail message
- Next, we implemented the election protocol by creating methods to:
  - send out request vote rpcs
	- reply to request vote rpcs, with the replica's voting decision
	- reply to a replica's voting decision, and potentially send out a leader elected message
	- update term and new leader once leader is elected
- Once leader election was working, we added the ability to redirect a client's request if the replica is not the leader
- Next, we added election timeout to occur and act as a leader failure. This starts a new election
- We implemented sending out heartbeats from the leader, and when replica's receive a heartbeat they restart their election timeout as well
- Lastly, we implemented adding client requests to a log and to state machine and responding to a client accordingly

## Testing
- To test we ran simple-1, simple-2 and crash-1
