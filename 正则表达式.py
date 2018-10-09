# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:32:22 2018

@author: DELL
"""
#验证输入用户名和qq号是否有效并给出对应的提示信息
'''
要求：
用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
QQ号是5~12的数字且首位不能为0
'''
import re

def main():
    username = input('请输入用户名：')
    qq = input('请输入qq号：')
    #match函数的第一个参数是正则表达式字符串或正则表达式对象
    #第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('请输入有效的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请输入有效的QQ号')
    if m1 and m2:
        print('你输入的信息是有效的！')
        
if __name__ == '__main__':
    main()
    
    
#从一段文字中提取出国内手机号码
'''
国内三家运营商的号码
电信：133/153/180/181/189/177;
联通：130/131/132/155/156/185/186/145/176;
移动号码：134/135/136/137/138/139/150/151/152/157/158/159/182/183/184/187/188/147/178
'''
import re

def main():
    #创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。 
    '''
    #查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print('----------华丽的分割线-----------')
    #通过迭代器取出匹配并保存
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('-----------华丽的分割线-----------')
    #通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())
        
if __name__ == '__main__':
    main()


#实现字符串倒转的方法
from io import StringIO

def reverse_str1(stri):
    return stri[::-1]

def reverse_str2(stri):#递归
    if len(stri) <=1:
        return stri
    return reverse_str2(stri[1:]) + stri[0:1]

def reverse_str3(stri):
    #StringIO对象是python中的可变字符串
    #不应该使用不便字符串连接操作 因为会产生很多无用字符串对象
    rstr = StringIO()
    str_len =len(stri)
    for index in range(str_len-1,-1,-1):
        rstr.write(str[index])
    return rstr.getvalue()










































    
    
    
    
    
    
    
