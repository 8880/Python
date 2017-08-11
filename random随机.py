#!/usr/bin/python
import random
x = random.randint(1,100)
print("—————————————————————欢迎进入死亡猜数游戏————————————————————")
a = input("请输入你的数字:\n")
guess = int (a)
while guess:
    if guess == x:
        print("恭喜你！猜对了")
        print("very good!")
        break
    else:
        if guess > x + 20:
            print("友情提示:数字过大")
        else:
            if guess < x - 20:
                print("友情提示:数字过小")
            else:
                if guess > x and guess < x + 20:
                    print("离成功不远了！大了点")
                else:
                    print("成功近在咫尺！小了点")
    a = input("再来过！")
    guess = int(a)
print("————————————————————游戏结束，你已经死了。————————————————————")
