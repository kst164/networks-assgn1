# Depiction of Internet Topology

## Authors:
- ### Abhay Shankar K: cs21btech11001
- ### Kartheek Sriram Tammana: cs21btech11028
- ### Kushagra Gupta: cs21btech11033


## Files
This section contain the list of files included, as well as their purposes and their origin.
- `data_collection`:
  - `raw_traces`:
  - `clean_traces`:
  - `01-traceroute.py`:
  - `02-collectASNs.py`:
  - `03-clean-raw-traces.py`:
  - `04-build-graph.py`:
  - `as_info.json`:
  - `graph.json`:
  - `ip_to_asn.json`:
- `viz`:
  - `src`:
  - `as_info.json`:

## Execution
This section contains the entire process to construct the final graph from scratch.

**Bunch of .py things**

## Presentation

Our final presentation is an interactive 3d graph, with each node representing a collection of routers and servers with the same AS number, and each edge representing a link between two routers with different AS numbers. 

We chose colleges across the globe as our destination - some of them have hosted their websites locally and independently, others have used a third-party service or CDN. This variation enables us to get a more complete picture of the Internet.

### Node properties:
- Each node represents one or more switches and routers. They have beenn condensed into a single node to prevent overpopulation, as well as achieve a more abstract representation - one node is one Autonomous System. It's that simple!
- Each node in the graph is labelled with its AS number, and upon hovering over a node a popup displays the same, along with the name of the corresponding institution or ISP.
- The nodes are also grouped by country, i.e. the colour of a node is determined by the country of the corresponding ASN.
- Nodes are also scaled in size based on their degree (i.e. number of incident edges). This facilitates a more intuitive understanding of network architecture.

### Edge properties:
- If two nodes are connected by an edge, then one of the routers or switches in the AS of the first node is directly connected to another in the AS of the second. These represent links between different autonomous systems. 
- We have chosen not to display the links that shunt packets around within an AS, as these generally represent the connections within a data centre.
- Each edge contains packets - animated spheres travelling along the edge direction. The rate of emission and the speed of these packets along the edge is representative of the time taken by a packet to complete it's journey within the AS of the recipient node, and not just the speed of the link joining the two Autonomous Systems.
- The graph is not a simple graph, and more than one edge may exist between two nodes. This occurs when `traceroute`s to multiple targets or from multiple sources. This is not directly visible, and appears as packets of different colours, travelling at different speeds. 

### Global graph properties
- The whole graph is interactive, and a user can drag a node around and hover over a node to get additional data. 
- Furthermore, the user may select a source or destination to highlight the nodes and edges constituting the path between them.
- The graph contains **48** nodes and **942** edges - some of these edges are between the same pair of nodes along different routes.

## Takeaways
- The Internet is a vast and complex realm, with myriad interconnected networks and subnetworks and a grand superstructure. Through the controlled application of the `traceroute` tool, we have been able to map a portion of the Internet to a graph, through which we study its topology.
- Numerically, looking at the edge-to-node ratio, we can see that the graph is dense and well connected. Obviously, not all the edges of the graph correspond to different physical links, but the number is a viable yardstick for how well-connected different parts of the network are.
- The first tangible takeaway is the knowledge of Autonomous Systems and their layout throughout the internet. The various APIs and online databases relating AS numbers to IPs and organisations yields valuable knowledge about the contents of the Internet.
- It is immediately obvious from the graph that a large amount of traffic goes through several key AS'es, and that these AS'es are ISPs or Cloud platforms. Further investigation shows the likes of Bharti Airtel, Reliance Jio Infocomm Ltd., along with Fastly.net and Cloudflare, Inc. which are Cloud platforms. 
- A more thorough review provides knowledge of ISP-client relations across the globe, including but not limited to the scope of the National Knowledge Network, exactly which ISPs service which organisations, and the fact that our college IITH is directly linked to several other IIT's directly without going through either NKN or Jio.
- The graph lends itself well to a deep investigation, which when conducted imparts several more insights. NKN itself appears to own two ASNs, viz. 55824 and 55847. However, when we check the ASN of IIT Guwahati, it shows 55847, indicating that this AS hosts some IIT websites. During our data colection, we found that IIT Kharagpur is also hosted in the same AS. 