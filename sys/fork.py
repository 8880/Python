#!/usr/bin/python
# -*-coding:utf-8 -*-

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print "create process faile"
elif pid == 0:
    print pid
    print "This is a child process",os.getpid()
else:
    sleep(0.01)
    print pid
    print "This is parent process",os.getpid()

print "一一一一一一一一一一一一一一一一"
