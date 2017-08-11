#!/usr/bin/python

class Base(object):
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        print('A.__init__ begin')
        Base.__init__(self)
        print('A.__init__ end')

class B(Base):
    def __init__(self):
        print('B.__init__ begin')
        Base.__init__(self)
        print('B.__init__ end')

class C(A,B):
    def __init__(self):
        print('C.__init__ begin')
        A.__init__(self)
        B.__init__(self)
        print('C.__init__ end')

c = C()

print C.__mro__
