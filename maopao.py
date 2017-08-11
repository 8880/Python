#!/usr/bin/python

l = [3,4,8,1,9,2,5,7]

n = len(l)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 -i:
        if l[j] > l[j + 1]:
            l[j],l[j + 1] = l[j + 1],l[j]
        j += 1
    i += 1
print l
