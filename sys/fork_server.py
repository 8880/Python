#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket,traceback,os,sys

host = '192.168.0.161'
port = 9999

s = socket.socket()             #创建套接字
s.bind((host,port))             #绑定地址（主机，端口号对）到套接字
s.listen(5)                      #开始 TCP 监听

while True:
    c,addr = s.accept()          #被动接受 TCP 客户的连接， （阻塞式）等待连接的到来

    pid = os.fork()

    if pid:
        c.close()
        continue
    else:
        s.close()
        while True:
            data = c.recv(1024).decode()
            if not len(data):
                break;
            print(data)
            c.send('recv your message'.encode())
        c.close()
        sys.exit(0)
