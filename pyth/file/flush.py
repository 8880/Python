#coding=utf-8

f = open('file','a')
print >>f,'增加一行'

f.flush()          #刷新缓冲区
