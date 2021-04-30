## High Level Approach Milestone
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

## High Level Approach Final Project
- We implemented correct usage of the AppendEntryRPC by sending data to the followers to be replicated into their key value stores
	- This included keeping track of quorums, replying to AppendEntryRPC's correctly, apply entries to the leader's state and responding to the client
- Within the implementation of replying to an AppendEntryRPC, the follower decides whether to respond with a success (saying that the log was committed to the kv store) or with a false
- If the follower responds with a failure then the leader must implement

## Testing
- To test we ran simple-1, simple-2 and crash-1
