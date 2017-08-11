#!/usr/bin/python
a = input("请输入一个数字:")
guess = int(a)
while guess:
        if guess > 5:
            print("数字过大")
        else:
            if guess < 5:
                print("数字过小")
            else:
                print("回答正确")
                break
        a = input("请重新输入一个数字:")
        guess = int(a)
print("游戏结束")
