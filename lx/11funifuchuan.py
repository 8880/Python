#!/usr/bin/python

def fun(x,y):
    s = ""
    for i in y:
        if i != x:
            s = s + i
    print s

a = 'l'
b = 'hello world'
fun(a,b)
