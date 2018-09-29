# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:21:33 2018

@author: DELL
"""
'''
'r':读取
'w':写入（会截断之前的内容）
'x':写入，如果文件存在会产生异常
'a':追加，将内容写入到已有文件的末尾
'b':二进制模式
't':文本模式（默认）
'+':更新（既可以读又可以写）
'''


'''
#读文件
def main():
    f = None
    try:
        f = open('D:\Desktop\交易大赛管理文档.docx','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:#总是执行代码块
        if f:
            f.close()#释放掉程序中获取的外部资源
            
def main():
    try:#指定文件上下文环境，并在离开上下文环境时自动释放文件资源
        with open('D:\Desktop\交易大赛管理文档.docx','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')        
if __name__ == '__main__':
    main()
    
#用for-in循环逐行读取 或者 用readlines方法将文件按行读取到一个列表容器中    
'''

'''
#1~99之间的素数保存在a.txt中，100~1000的素数保存在b.txt中，1000~10000的保存在c.txt中
from math import sqrt

def is_prime(n):
    '''判断素数的函数'''
    assert n>0
    for factor in range(2,int(sqrt(n))+1):#开方加一
        if n% factor ==0:
            return False
    return True if n !=1 else False

def main():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename,'w',encoding='utf-8'))
        for number in range(1,10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number)+ '\n')#保存在a.txt中
                elif number < 1000:
                    fs_list[1].write(str(number)+'\n')
                else:
                    fs_list[2].write(str(number)+'\n')
                    
    except IOError as ex:
        print(ex)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')
    
if __name__ == '__main__':
    main()


'''
#将字典或列表以json格式保存到文件中
'''
dump - 将python对象按照json格式序列化到文件中
dumps - 将python对象处理成json格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成python对象
'''
import json
def main():
    mydict ={
        'name':'df',
        'age':38,
        'qq':957658,
        'friends':['王大锤','白元芳'],
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand':'Audi','max_speed':280},
            {'brand':'Benz','max_speed':320}
                ]
            }
    try:
        with open('data.json','w',encoding='utf-8' as fs):
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')
    
if __name__ == '__main__':
    main()
    
    
            




















































 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    