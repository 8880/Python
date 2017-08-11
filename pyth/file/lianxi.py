import time
from datetime import datetime
from time import sleep
from time1 import n
n

while True:
    sleep(1)
    f = open('test.txt','a')
    n += 1
    print >>f,n, datetime.now()
    f1 = open('time1.py','w')
    print >>f1,'n =',n
