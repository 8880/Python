#!/usr/bin/python

def fum(x):
    return x ** 2

def funf(x):
    return x > 2 and x < 5

def funr(x,y):
    return x + y

l = [1,2,3,4,5]

print map(fum,l)

print filter(funf,l)

print reduce(funr,l)

#zip
