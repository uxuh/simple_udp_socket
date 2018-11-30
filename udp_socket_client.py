#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""a socket example which send echo message to server."""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# when connected, only receive data from port number 9999.
s.connect(('127.0.0.1',9999))
# After connected, we also got a port number.
# If not use connect(), bind(('', 0)) can be used to get a port number.
# s.bind(('', 0))

local_addr = s.getsockname()    # getsockname() return the address with port number
print('local address is ', local_addr)

for data in ['Michael', 'Tracy', 'Sarah']:
    # Send
    # udp connected, then send() to connected port.
    s.send(data.encode())
    # If not connected, then use sendto()
    # s.sendto(data.encode(), ('127.0.0.1', 9999))

    # Receive
    rx_data = s.recvfrom(1024)
    print(rx_data[0].decode(), 'from', rx_data[1])

    # recv() only return received data
    # print(s.recv(1024))
s.close()

