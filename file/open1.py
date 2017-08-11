#coding=utf-8
import sys

with open('file1','r+') as f:
    print >>f,"东临碣石,以观沧海"          #print('东临碣石,以观沧海',f)
print >>sys.stdout,"东临碣石,以观沧海"
print >>sys.stderr,"东临碣石,以观沧海"
# print >>sys.stdin,"东临碣石,以观沧海"
