#!/usr/binpython
#coding=utf-8
from time import sleep

f = open('talk')

boss = []
god = []

for i in f:
    if i[:6] != '======':
        (name, talk) = i.split('：', 1)
        print talk
        if name == '老板':
            boss.append(talk)
        elif name == '顾客':
            god.append(talk)
    else:
        f1 = open('talk1','w')
        f1.writelines(boss)
        f1.writelines(god)
        f1.close()
f.close()
