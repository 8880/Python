#!/usr/bin/python

from socket import *
from time import ctime
import sys

HOST = '192.168.0.161'
PORT = int(sys.argv[1])   #8884
BUFSIZE = 1024
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(ADDR)

while True:
    print "wating for connection...."

    data, addr = sockfd.recvfrom(BUFSIZE)

    print "client adder :", addr

    sockfd.sendto("[%s] : %s"%(ctime(),data), addr)

sockfd.close()
