# Cloud1x2Bet
Cloud Computing Project

Team Members:
- Bogdan Nutu - SCPD
- Daniel Dinca - SCPD
- Iuliana Brinzoi - SCPD

How to run the project:
- run ./start-services.sh
  This will create the following containers:
    - cloud1x2bet_client_1
    - cloud1x2bet_auth_1
    - cloud1x2bet_service_1
    - cloud1x2bet_admin_1
    - cloud1x2bet_adapter_1
    - cloud1x2bet_influxdb_1
    - cloud1x2bet_db_1
    - cloud1x2bet_grafana_1
    
- run ./start-client.sh
    This will attach to the client. Then, you can follow the instructions in order to use the app.
    
- run ./reset-services.sh
  This will stop all the containers and remove all local volumes.
 
