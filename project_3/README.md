# Milestone 1

## Milestone 1 Approach

We implemented two things for milestone 1:

- We created the routing table as a list of ForwardingTableEntries, each of which contained a network, netmask, srcif (interface describing the socket). We then implemented an update function which, given an update message, will add an entry to our routing table.
- We implemented the forward and dump functions to pass on messages we received and print out the forwarding table

## Milestone 1 Testing

- We tested using the given milestone tests.

# Project 3

## Approach

- After completing the milestone we worked expanded our forwarding table to include the other attributes necessary for selecting a path if there are multiple options.
- Then we implemented the rules to select a path and added the case where there is no route possible.
- We implemented the revoke message, and revoking the forwarding table entries that matched the networks in the revoking message.
- We enforced peering, provider and customer relationships, this impacted which networks receive the revoking/updating messges. If the source is a customer = everyone receives the message, if not only the customer receives the message.
- We expanded the forwarding table to include longest prefix matching.
- Lastly, we implemented route aggregation by checking if routes are adjacent and have matching attributes. Then implemented route disaggregation by throwing out the table and applying the update/revoke messages to rebuild the table.

## Project 3 Testing

- We tested using the given project tests, ensuring that each level passes before continuing to the next level.
