#!/usr/bin/python

l = [[5,2,4,3],[4,9,2,8],[5,1,1,20]]

for i in l:
    for j in i:
        print j,
    print ""

out = len(l)
inl = len(l[0])

i = j = 0
x = y = 0
maX = l[0][0]

while i < out:
    j = 0
    while j < inl:
        if l[i][j] > maX:
            maX = l[i][j]
            x,y = i,j
        j += 1
    i += 1

print "max[%d][%d]=%d"%(x,y,maX)
