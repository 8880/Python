#!/usr/bin/python

i, j = 1, 1

while i < 10000:
    print i,
    i, j = j, i+j
