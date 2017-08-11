#!/user/bin/python
#coding=utf-8

def fun_out():
    a = 4
    def fun_in():
        nonlocal a               #python3专用,nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        a += 1                   #主要是在函数嵌套中的内层函数使用外层函数的变量如果不加nonlocal
    fun_in()                     #可以打印但是不能修改，时候这个标记后可以修改。
    print (a)

fun_out()
