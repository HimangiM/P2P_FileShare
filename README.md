# P2P_FileShare

#### Ping the Ubuntu PC you want to connect to
      ping -c 4 <IP address of the other PC>
      This command will send 4 packets to the desired PC.
   
#### Open any random port. This will be reserved for the connection to the PC.
      Check the status of the ports using : sudo ufw status verbose
      Now, open any random port using : sudo ufw allow <port number>
      Check the status again to see if your entered port number has opened (STATUS : ALLOW IN) is there.
  
