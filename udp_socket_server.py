#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" a udp server example
    rx socket use a fixed port number 9999
    tx socket is not fixed

"""

import socket

s_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s_1.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s_1.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # try to use a different port number send back to client
    # s_2.sendto(('Hello! %s from different port' %data.decode()).encode(), addr)
    s_1.sendto(('Hello! %s' %data.decode()).encode(), addr)

