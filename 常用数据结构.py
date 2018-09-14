# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:45:16 2018

@author: DELL
"""

#使用字符串
def main_string():
    str1 = 'hello,world!'
    print(len(str1))#获取字符串的长度
    print(str1.capitalize())#获取首字母大写的拷贝
    print(str1.upper())#获取字符串变大写后的拷贝
    print(str1.find('or'))#从字符串中查找子串所在的位置
    print(str1.index('or'))#从字符串中查找子串所在的位置
    print(str1.startswith('He'))#是否以He开头
    print(str1.endswith('!'))#是否以！结尾
    print(str1.center(50,'*'))#以指定的宽度居中并在两侧填充指定的字符
    print(str1.rjust(50,'*'))#将字符串以指定的宽度靠右放置，左侧填充指定的字符
    
    str2 = 'abc123456'
    print(str2[2])#从字符串中取出指定位置的字符
    print(str2[2:5])#取第二个到第四个
    print(str2[2:])#取第二个到最后一个
    print(str2[2::2])#取第二个到最后一个，步长为2
    print(str2[::2])#取第0个到最后一个，步长为2
    print(str2[::-1])#倒着数
    print(str2[-3:-1])#取倒数第二个至倒数第三个
    print(str2.isdigit())#判断字符串是否由数字构成
    print(str2.isalpha())#判断字符串是否以字母构成
    print(str2.isalnum())#判断字符串是否以字母和数字构成
    print(str2.strip())#去字符串两边的空格
    
    
#使用列表
'''
定义列表、使用下标访问、添加和删除元素
'''
def main_list1():
    list1 = [1,3,5,7,100]
    print(list1)
    list2 = ['hello']*5
    print(list2)
    print(len(list1))#计算列表长度
    print(list1[0])#下标运算
    print(list1[-1])#取最后一个
    list1[2] =300#重新赋值
    list1.append(200)#在列表最后添加单个元素
    list1.insert(1,400)#在第一个元素的位置插入400
    list1 += [1000,2000]#在列表最后添加多个元素
    list1.remove(3)#删除列表中3这个元素
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]#删除第一个元素
    list1.clear()#清除列表中的元素
'''
列表的切片操作
'''
def main_list2():
    fruits = ['grape','apple','strawberry','waxberry']
    fruits += ['pitaya','pear','mango']
    for fruit in fruits:
        print(fruit.title(),end=' ')#title 所有单词都是以大写开始
    fruits2 = fruits[1:4]#列表切片
    fruits3 = fruits#创建了新的引用,并没有复制列表
    fruits4 = fruits[:] #可以通过完整切片操作来复制列表
    fruits5 = fruits[-3:-1]
    fruits6 = fruits[::-1]#可以通过反向切片来获取倒转后的列表的拷贝
    
'''
列表的排序
'''   
def main_list3(): 
    list1 = ['orange','apple','zoo','internationalization','blueberry']
    list2 = sorted(list1)#返回列表排序后的拷贝，不会修改传入的列表
    list3 = sorted(list1,reverse=True)#降序
    list4 = sorted(list1,key=len)#根据字符串长度进行排序（默认字母排序）
    list1.sort(reverse=True)#直接在列表对象上进行排序

'''
用列表的生成表达式语法创建列表容器
用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
'''
import sys
def main_list4():
    f1 = [x for x in range(1,10)] #生成式
    f2 = [x + y for x in 'ABCDE' for y in '1234567']  
    f3 = [x ** 2 for x in range(1,1000)]
    print(sys.getsizeof(f3)) #查看对象占用内存的字节数
    '''
    下面的代码创建的不是一个列表而是一个生成器对象
    通过生成器可以获取数据但他不占用额外的空间存储数据
    每次生成数据的时候就通过内部的运算得到数据
    '''
    f4 = (x ** 2 for x in range(1,1000))#生成器
    print(sys.getsizeof(f4))#相比生成式，生成器不占用存储数据的空间
    for val in f4:
        print(val)

    
    
#使用元组（与列表相似 但是不能修改）[一般用于存放不需要修改的变量]
def main_tuple():
    t = ('骆昊',38,True,'四川成都')
    print(t[0])
    for i in t:
        print(i)
    #t[0] = 'simoon'修改会有typeerror
    t = ('王大锤',20,True,'云南昆明')
    person = list(t)#将元组转换成列表，列表是可以修改的
    person[0] = '李明'
    person[1] = 25
    print(person)
    fruits_list = ['apple','banana','orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    
#使用集合（不允许有重复元素，但可以进行交集并集差集等运算）
def main_set():
    set1 = {1,2,3,3,3,2}
    print(set1)
    print('Length =',len(set1))
    set2 = set(range(1,10))  
    print(set2)  
    set1.add(4)
    set1.add(5)
    set2.update([11,12])    
    print(set1)
    print(set2)
    set2.discard(5)#删除元素，如果没有也不会报错
    if 4 in set2:
        set2.remove(4)#删除元素，如果没有会报错
    for elem in set2:
        print(elem **2,end = ' ')
    #将元组转化为集合
    set3 = set((1,2,3,3,2,1))
    print(set3.pop())
    print(set3)
    '''
    集合的交集、并集、差集、对称差运算
    判断子集和超集
    '''
    print(set1 & set2)#print(set1.intersection(set2))交集
    print(set1 | set2)#print(set1.union(set2))并集
    print(set1 - set2)#print(set1.difference(set2))差集
    print(set1 ^ set2)#print(set1.symmetric_difference(set2))对称差
    print(set2 <=set1)#print(set2.issubset(set1))判断是否为子集
    print(set2 >=set1)#print(set2.issuperset(set1))判断是否为超集
    
#使用字典（可变容器，由键值对组成）
def main_dict():
    scores = {'骆昊':95,'白远方':78,'狄仁杰':82}
    print(scores['骆昊'])#通过键获取值
    for elem in scores:#遍历字典
        print('%s\t--->\t%d'%(elem,scores[elem]))
    scores['白远方'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67,方启鹤=85)#添加新的键值对
    print(scores.get('武则天'))#通过键对获取对应的值
    print(scores.get('武则天',60))#可以设置默认值
    print(scores.popitem())
    print(scores.pop('骆昊',100))#值错了也可以删除
    scores.clear()#清空字典


'''
练习
'''
#在屏幕上显示跑马灯文字
import os
import time
def screen_show():
    content = '北京欢迎你为你开天辟地......'
    while True:
        #清理屏幕上的输出
        os.system('cls')
        print(content)
        #休眠200毫秒
        time.sleep(0.2)
        content = content[1:]+content[0]
    
#生成指定长度的验证码
import random
def verification_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    last_pos = len(all_chars) -1
    code = ''
    for i in range(code_len):
        index = random.randint(0,last_pos)
        code +=all_chars[index]
    return code    
        
#设计一个函数 返回给定文件名的后缀
def get_suffix(filename):
    if '.' in filename:
        name = filename.split('.')[1]
        print('文件的后缀名为：',name)
    else:
        print('文件没有后缀名')
        
#设计一个函数返回传入的列表中的最大和第二大的元素的值
def max2(x):
    y = sorted(x,reverse=True)
    print('列表中最大的数是%d'%y[0])
    print('列表中第二大的数是%d'%y[1])

#计算指定的年月日是这一年的第几天
def which_day(year,month,day):
    if year % 4 ==0 and year % 100 !=0 or year % 400 ==0:
        day_of_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(month-1):
        total += day_of_month[i]
    total = total +day
    print('%d年%d月%d日是这一年的第%d天'%(year,month,day,total))
        
#打印杨辉三角
def yanghui_triangle():
    num = int(input('Number of rows:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row+1)
        for col in range(len(yh[row])):
            if col ==0 or col == row:#是每行的第一个或者是最后一个
                yh[row][col] = 1#他的值就为1
            else:#否则就是上一行该列的值加上上一行前一列的值
                yh[row][col] = yh[row -1][col] +yh[row -1][col -1]
            print(yh[row][col],end='\t')
        print()

#约瑟夫环问题
'''
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将15个人扔到海里面
有一个人想了一个办法就是大家围成一个圈，有某人开始从1报数，报到9的就扔海里面，他后面的人接着从1开始报数
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑。15个基督徒都幸免遇难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒
'''
def joseph():
    people_index = [i for i in range(1,31)]
    people_throwed = 0
    while people_throwed<15:
        people_index = people_index[9:] +people_index[0:8]
        people_throwed +=1
    print(people_index)
        
        

    

































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    