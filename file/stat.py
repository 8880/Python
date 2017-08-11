#coding=utf-8
import os
import time

filename = raw_input('file name:')     #输入查看文件的名字

file_stat = os.stat(filename)

print file_stat

print time.localtime(file_stat.st_ctime)
