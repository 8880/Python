#!/usr/bin/python

for i in range(1,100):
	f = 0
	for j in range(2,i/2):
		if (i % j == 0):
			f = 1
	if f == 0:
            print i
