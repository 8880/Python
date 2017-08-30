#!/usr/bin/python
#coding=utf-8

b = 5 ; c = 0

for i in range(1,4):
    a = input("请输入数字:")
    if a == b:
        print("对")
        c = 1
        break
    else:
        print("错")
if c == 0:
    print("3次结束")
