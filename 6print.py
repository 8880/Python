#!/usr/bin/python
#coding=utf-8

print 1                               #固定整数数值
print 1.2                           #浮点型小数
print "hello"                    #字符串
print [1,2,3,4,5]              #列表形式
print (1,2,3,4,5)                #元组形式
print {1,2,3,4,5}                   #集合型
print {'a':1,'b':2}                    #字典型

print "---------------------"
a = "hello"

print a

print "key:",a,"!!!",         #后面加逗号表示不换行
print "test"

b = 1
c = 1.25745

print "a = %s,b = %d !!!"%(a,b)
print '---------------------------'

print "%.2f"%c                   #保留2位小数
print "%10f"%c                #总共有10位数,小数点后保留6位，不够的补0，小数点前面的数补空格
print "%10.f"%c            #共10位数，保留0位小数，前面补空格
print "%10.3f"%c         #共10位数，保留3位小数
print "%09.4f"%c           #共9位数，保留4位小数，不够的补0
print "%+09.2f"%c            # + 表示 该数值的正负情况
print "%-10.3f"%c              # - 表示左对齐
print "%.*f"%(3,c)               #保留3为小数，*表示不确定，括号里的3决定
