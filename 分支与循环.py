# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:05:13 2018

@author: DELL
"""
'''
分支结构的应用
'''
#分段函数求值
def Piecewise_function():   
    x = input("please enter the number")
    flag = True
    while flag:
        try:
            y = float(x)
            flag = False
        except:
            x = input("please enter the right number")
    f = 0
    if y>1:
            f = 3*y -5
    elif y <-1:
            f = 5*y +3
    else:
            f = y +2
    print("f(%d) = %d"%(y,f))
        
    
#打印1到100这些数字，遇到3的倍数时用“Fizz”替代。遇到5的倍数时用“Buzz”代替，既是3又是5的倍数打印“FizzBuzz”
def one_hundred():
    l = [i+1 for i in range(100)]
    for i in range(len(l)):
        if l[i]%3 ==0 and l[i]%5 !=0:
                l[i] = 'Fizz'
        elif l[i]%5 ==0 and l[i]%3 !=0:
                l[i] = 'Buzz'
        elif l[i]%3 ==0 and l[i]%5 ==0:
                l[i] = 'FizzBuzz'
    print(l)
    

#输入n,求n!并输出
def Factorial():
    n = float(input("please enter a number:"))
    def func(n):
        if n<1:
            return 1
        else:
            return n*func(n-1)
    f = func(n)
    print(f)
    

#输入十个整数，找出最大数
def find_max():
    l = []
    for i in range(10):
        x = float(input("please enter a number"))
        l.append(x)
    max1 = l[0]
    for i in range(len(l)):
        if max1 <l[i]:
            max1 = l[i]
    print(max1)
        
    
#输入一个数判断是否是素数
def prime_judger():
    is_prime = True
    n = int(input("please enter a number:"))
    if n>2:
        for i in range(2,n):
            if n%i == 0 :
               is_prime = False
               break
            else:
               is_prime = True 
    else:
        is_prime = False
    if is_prime == True:
        print("%d是素数"%n)
    else:
        print("%d不是素数"%n)
        
#输入两个正整数，计算最大公约数和最小公倍数
def divisor_multiple():
    x = int(input("please enter a number:"))
    y = int(input("please enter another number:"))
    if x>y:#把小的那个值找出来
        (x,y)=(y,x)
    for factor in range(x,0,-1):#从大的往小的数
        if x %factor ==0 and y %factor ==0:
            print("%d和%d的最大公约数为%d"%(x,y,factor))
            print("%d和%d的最小公倍数为%d"%(x,y,x*y//factor))#取整除  
            break


#打印三角形图案
def triangle():
    row = int(input("please enter the row:"))
    for i in range(row):
        #print((i+1)*'*'+' '*(row-i-1))
        #print(' '*(row-i-1)+'*'*(i+1))
        print(' '*(row-i-1)+(2*i+1)*'*'+' '*(row-i-1))
        
#百钱百鸡 一只公鸡5元 一只母鸡3元 3只小鸡1元 用100元买100只鸡 问公鸡 母鸡 小鸡各有多少只
def hundred_chicken():
    for x in range(20):
        for y in range(33):
            z = 100-x-y
            if 5*x + 3*y +z/3 == 100:
                print('公鸡：%d只,母鸡：%d只,小鸡：%d只'%(x,y,z))
                
    
#Craps赌博游戏
'''
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇到2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次摇色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
'''
from random import randint 
def craps():
    money = 1000
    while money >0:
        print('你的总资产为:',money)
        needs_go_on = False
        while True:
            debt = int(input('请下注：'))
            if debt >0 and  debt <= money:
                break
        first = randint(1,6)+ randint(1,6)
        print('玩家摇出了%d点'%first)
        if first ==7 or first ==11:
            print('玩家胜！')
            money += debt
        elif first ==2 or first ==3 or first ==12:
            print('庄家胜！')
            money -= debt
        else:
            needs_go_on = True
            
        while needs_go_on:
            current = randint(1,6)+randint(1,6)
            print('玩家摇出了%d点'% current)
            if current ==7:
                print('庄家胜')
                money -=debt
                needs_go_on = False
            elif current == first:
                print('玩家胜')
                money +=debt
                needs_go_on = False
    print('你破产了，游戏结束')

    
#斐波那契数列   
'''
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
'''  
def Fibonacci():
    a =0
    b =1
    for i in range(20):
        (a,b) = (b,a+b)
        print(a,end = ' ')      

#水仙花数
'''
找出100-999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
比如： 153 = 1**3 + 5**3 + 3**3
'''
def lily():
    lily = []
    for i in range(100,1000):
        hundred = i//100
        ten = (i -hundred*100)//10
        position = (i -hundred*100-ten*10)
        if i == pow(hundred,3)+pow(ten,3)+pow(position,3):
            lily.append(i)
    print('水仙花数有',lily)
    
#回文数
'''
判断输入的正整数是不是回文数
回文数是指将一个正整数从左到右和从右到左排列值一样的数
'''
def palindrome():
    number = input("please input a number")
    return number == number[::-1]
    

#完美数
'''
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如：6 = 1+2+3 ,28 = 1+2+4+7+14
'''      
def perfect():
    for i in range(1,10000):
        perfect = []
        for n in range(1,i):
            if i%n ==0:
                perfect.append(n)
        numb = 0
        for m in perfect:
            numb +=m
        if numb ==i:
            print('%d是完美数'%i)
            
            
            
#输出九九乘法表
for i in range(1,10):
      for j in range(1,10):
          print('%d*%d=%d' %(i,j,i*j),end= '\t')
      print()
            
                    
                

            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    