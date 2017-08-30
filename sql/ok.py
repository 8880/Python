#!/usr/bin/python
#coding=utf-8

import MySQLdb
try:
    db = MySQLdb.connect('localhost','root','123','shuju')   # password 也可以直接填写密码
except ProgrammingError:
    exit(1)

cursor = db.cursor()
cursor.execute("select version()")

a = 1;
while a > 0:
    print'                 ------------------------------------------------------------'
    print'                 |  1: insert   2: delete   3: update   4: select   5: quit |'
    print'                 ------------------------------------------------------------'

    num = input('请输入：')

    if num == 1:
        dd = input('id(int)')
        name = raw_input('name(char)')
        age = input('age(int)')
        sorce = input('sorce(float)')

        sql = '''insert into biaodan (id,name,age,sorce) values (%d,'%s',%d,%f)'''%(dd,name,age,sorce)
        cursor.execute(sql)
        db.commit()

    if num == 2:
        s = input('输入删除的id：')
        sql = '''delete from biaodan where id = '%d' '''%(s)
        cursor.execute(sql)
        db.commit()

    if num == 3:
        u = input('输入需要更改的id：')
        n = raw_input('更改的项目：')
        g = raw_input('更改的内容：')

        sql = '''update biaodan set %s = '%s' where id = %d;'''%(n,g,u)
        cursor.execute(sql)
        db.commit()

    if num == 5:
        break

    if num == 4:
        cursor.execute("select * from biaodan")

        date = cursor.fetchall()
        #print data

        for i in cursor.description:
            print i[0],

        print ""

        for row in date:
            for i in row:
                print i,
            print ""

    if num == 6:
            print'       ------------------------------------------------------------------------------'
            print'       |  1: id查找   2: name查找   3: age查找   4: sorce查找   5:全部查看   6:  退出查找 |'
            print'       ------------------------------------------------------------------------------'
            num1 == input('请输入:')
            if num == 1:
                v = input("请输入ID:")
                sql = '''select * from biaodan '''
