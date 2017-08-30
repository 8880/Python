#!/usr/bin/python

def fun(l):

    for i in range(len(l)):
        j = 0
        for j in range(len(l) - 1):
            if l[j] % 2 == 0:
                l[j],l[j + 1]=l[j + 1],l[j]
    print l

l = [4,2,7,5,8,9,31,34,66,12,99,55]

fun(l)
