#!/usr/python

for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print "%dx%d=%d"%(j,i,i*j),
        else:
            print "\n"
            break
