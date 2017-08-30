#!/usr/bin/python
#coding=utf-8

import MySQLdb
import getpass

password = getpass.getpass("please input your password:")

#打开数据库链接
try:
    db = MySQLdb.connect('localhost','root',password,'klous')   # password 也可以直接填写密码
except ProgrammingError:
    exit(1)

#获取数据游标
cursor = db.cursor()

try:
    cursor.execute("select * from student")
    data = cursor.fetchone()
    print data
    data = cursor.fetchone()
    print data
    data = cursor.fetchone()
    print data
    data = cursor.fetchone()
    print data
    data = cursor.fetchone()
    print data
    data = cursor.fetchone()
    print data

    date = cursor.fetchall()
    #print data

    for i in cursor.description:
        print i[0],

    print ""

    for row in date:
        for i in row:
            print i,
        print ""

except:
    print 'error'
