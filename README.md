# outpost
Litestar based C2 for BOFs


My plan is to create a command and control framework specifically designed to handle Beacon object file style agent deployments from spear phishing attacks as the initial access vector



My general goal is to have a constantly expanding library of “droppers” which are designed to bypass AV/EDR 

From there they simply are able to query the http listener for a new task or .so/.DLL file to load and run 

The general goal is to create a team server that is made accessible to a client which will likely be the tor browser 

My goal is to have the team server exposed as a Jinja2 template based web service as a .onion address 







## **Tech Stack**
- Python
- [Litestar](https://litestar.dev/) for the backend
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) for the templating
- [Bulma](https://bulma.io/) for the styling
- Postgres for the database
- Redis for the task queue





## **Goals**:
- Create a Tor based Dashboard for the C2
- Agents communicate via HTTPS
- Multi Listener support for redundancy and segmentation
- Support "external C2", allowing for reverse proxying for agents to connect to the C2 (Tor2Web, Nginx, Cloudflare Oblivious HTTP Proxy, etc.)
- Agents are able to connect to the C2 via Tor, clearnet, or both (LONG TERM)
- Obfuscate the C2 infrastructure using Hugo based static sites to make things seem more legit
- Manage stagers + stager generation within the dashboard
- MAYBE add Git integration for managing the code for agents, stagers, object files, etc.
- internal build system for compiling the agents, stagers, object files, etc.




