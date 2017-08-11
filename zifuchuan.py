#!/usr/bin/python

str1 = 'xiaoxie'                       #将字符串的第一个字符变为大写
a = str1.capitalize()
print (a)

str2 = 'XIAOXIE'                      #把整个字符串的所有字符变为小写
b = str2.casefold()
print (b)

c = str2.center(168)                 #将字符居中，并使空格填充长度width为填充长度
print (c)

str3 ='i\tduzzzzyyyzz\to'           #把字符串中的tab符号(\t)转换为空格，如果不指定参数
d = str3.expandtabs(10)             # 默认的空格数是tabsize=8
print (d)
