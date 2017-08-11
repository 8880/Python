#!/usr/bin/python
#coding=utf-8

import dir1.module1                  #包的导入 每个目录下必须有__init__.py文件
from dir1 import module2

print dir1.module1.a

obj = dir1.module1.A()

obj.a()

dir1.module1.b()

a = 10

print "======================="

obj_d = module2.D()
obj_d.d()
print module2.b
