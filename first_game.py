# 第一个小游戏
import random
secret = 5 # 7random.randint(1,10)

temp = input ("猜一下现在心里想的是哪个数字：")
guess = int (temp)
times = 1

while (guess != secret) and (times < 3 ) :
    if guess < secret :
        print("猜错了，小了小了")
    else :
        print("猜错了，大了大了")
    
    temp = input ("再猜一下吧：")
    guess = int (temp)
    times = times + 1

if (guess == secret) and (times < 3) :
    print("终于猜对了，游戏结束！")
else :
    print("很遗憾，三次机会用光了！")


