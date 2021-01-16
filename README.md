# Cloud1x2Bet
Cloud Computing Project

Team Members:
- Bogdan Nutu - SCPD
- Daniel Dinca - SCPD
- Iuliana Brinzoi - SCPD

How to run the project:
- run ./start-services.sh --> 
  This will create the following containers:
    - cloud1x2bet_konga_1
    - cloud1x2bet_kong_1
    - cloud1x2bet_adminer_1
    - cloud1x2bet_service_1
    - cloud1x2bet_auth_1
    - cloud1x2bet_admin_1
    - cloud1x2bet_adapter_1
    - cloud1x2bet_influxdb_1
    - cloud1x2bet_kong_db_1
    - cloud1x2bet_grafana_1
    - cloud1x2bet_db_1

- go to http://127.0.0.1:1337/ in your browser.

- create admin account in Konga

- sign in Konga with the account that you have just created

- go to connections, in the left panel. click "new connection". set the name as "kong" and the kong admin url as "http://kong:8001". create a new connection. then, activate the new connection

- go to services, in the left panel

- add the following 4 services (edit just the name, host and port. leave the rest of the fields empty):
    1. Name: adminer, Host: adminer, Port: 8080
    2. Name: admin, Host: admin, Port: 5000
    3. Name: auth, Host: auth, Port: 5000
    4. Name: service, Host: service, Port: 5000
    
- click on "adminer" service. go to routes. click "add route" and add the following route: Name: to_adminer, Paths: /adminer. submit the new route
(important: after editing the paths as "/adminer", click enter. otherwise, you will get a submision error).

- do the same thing for auth, admin and service services. add a new route for each one, as follows:
    1. Name: to_auth, Paths: /auth --> auth
    2. Name: to_admin, Paths: /admin --> admin
    3. Name: to_service, Paths: /service --> service

- now, you can run the client. go to the terminal and run ./start-client.sh
    This will attach to the client. Then, you can follow the instructions in order to use the app.
    
- After using the app, you can stop and remove all the containers with ./reset-services.sh
