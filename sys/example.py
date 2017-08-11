#!usr/bin/python
import threading
from time import sleep

date = 0

def a(e):
    e.wait()
    global date
    date = 10
    sleep(0.5)
    print "process a :",date

def b(e):
    global date
    date = 100
    print "process b :",date
    e.set()

if __name__ == '__main__':
    e = threading.Event()
    w1 = threading.Thread(target = a, args = (e,))
    w1.start()

    w2 = threading.Thread(target = b, args = (e,))
    w2.start()

    print 'main : waiting befor calling Event.set()'
    sleep(2)
    print 'over'
