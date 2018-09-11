# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:26:07 2018

@author: DELL
"""

'''
global关键字用来在函数或其他局部作用域中使用全局变量
如果不修改全局变量也可以不使用global关键字
'''
gcount =0

def global_test():
    print(gcount)
    
def global_counter():
    global gcount
    gcount +=1
    return gcount

def global_counter_test():
    print(global_counter())
    print(global_counter())
    print(global_counter())
    
    
'''
nonlocal关键字用来在函数或其他作用域中使用外层（非全局）变量
'''
def make_counter():
    count =0
    def counter():
        nonlocal count
        count +=1
        return count
    return counter()

def make_counter_test():
    print(make_counter())
    print(make_counter())
    print(make_counter())


'''
生成器，迭代器
'''
#容器（可以是dict set tuple等）
assert 1 in [1,2,3]
assert 4 not in {1,2,3}
assert 4 in (1,2,3)
d = {1:'foo',2:'bar',3:'qux'}
assert 1 in d
assert 'foo' not in d
s = 'foobar'
assert 'b' in s
assert 'foobar' in s

#可迭代对象（同容器，可以是dict set tuple）
x = [1,2,3]
y = iter(x)
z = iter(x)
next(y)
next(y)
next(z)
type(x)
type(y)

#迭代器
'''
生成无限序列
生成从13开始的连续整数
'''
from itertools import count
counter = count(start=13)
next(counter)
'''
从一个有限序列中生成无限序列
cycle对iterable中的元素反复执行循环操作
'''        
from itertools import cycle
colors = cycle(['red','white','blue'])
next(colors)
next(colors)
'''
从无限序列中生成有限序列
itertools.islice(iterable,start,stop[,step])开始位置，结束位置，步幅
'''
from itertools import islice
colors = cycle(['red','white','blue'])
limited = islice(colors,0,4)
for x in limited:
    print(x)
'''
斐波那契数列
'''
class Fib:
    def __init__(self):
        self.prev =0
        self.curr =1
        
    def __iter__(self):#Fib是一个可迭代对象
        return self
    
    def __next__(self):#是一个迭代器 为下一次调用next()方法修改状态 为当前这次调用生成返回结果
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
    
f = Fib()
list(islice(f,0,10))



#生成器
'''
是一种特殊的迭代器，更优雅
不需要__iter__()和__next__()方法，只需要一个yield关键字
生成器一定是迭代器
'''
def fib():
    prev, curr = 0,1
    while True:
        yield curr
        prev, curr = curr, curr+prev
        
f = fib()
list(islice(f,0,10))











































