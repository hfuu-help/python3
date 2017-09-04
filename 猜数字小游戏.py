# -*- coding: utf-8 -*-
import random
#猜数字小游戏，你永远猜不到正确数字
s = random.randint(0,2) #生成随机数,括号内为随机数的范围
list_number = []

for i in range(1,10):#此处涉及一个range和xrange的知识点
    number = int(input("请输入0-9的整数："))
    list_number.append(number)
    #print(list_number)

    if i == 9:
        while s in list_number:
            s = random.randint(0,9)
        print('游戏结束，正确答案是%d'%s)
    print('回答错误，还剩下%d次机会'%(9-i))
