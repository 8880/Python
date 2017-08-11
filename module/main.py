#!/usr/bin/python
#!coding=utf-8

import module1 as m             # 把module1 用 as 变为 m
import module2
from module2 import D,b         #把指定的 导入本地空间，与import不同的地方是 会覆盖相同名称的变量
                                # from module2 import * 全部导入  不能导入 ”_“ 开头的
reload(m)                        #重复导入模块


print m.a

obj = m.A()

obj.a()

m.b()

print m.__doc__

obj2 = module2._C()

obj2.ss()

print "===================="
b = 10                # module2 中的b=10000 被 b=10覆盖掉
obj_d = D()
obj_d.d()
print b
