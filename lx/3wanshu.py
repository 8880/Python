#!/usr/bin/python

for i in range(1,1000):
    su = 0
    j = 1
    while j < i:
        if i % j == 0:
            su += j
        j += 1
    if su == i:
        print i
