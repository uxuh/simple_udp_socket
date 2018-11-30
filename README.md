# simple_udp_socket
a simple UDP socket

In udp socket client, when connect((ipaddr,port_number)) used, it will only receive data from this port_number.
If not use connect(), it will received data from any ports.

bind(('', 0)) can be used to get a port number from OS.
