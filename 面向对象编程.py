# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:19:56 2018

@author: DELL
"""

#定义类
class Student(object):
    #__init__方法用在创建对象时进行初始化操作，绑定属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print('%s正在学习%s' %(self.name,course_name))
    def eat(self):
        if self.age<10:
            print('eat less')
        else:
            print('eat more')
def main():
    stud1 = Student('kris',34)
    stud1.study('en')
    stud1.eat()
if __name__ == '__main__':
    main()

#访问可见性    
#如果希望属性是私有的就在属性前面用两个下划线作为开头
class Test:
    def __init__(self,foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print('__bar')
    def get_bar(self):#外部也是可以访问的
        return self.__foo

def main():
    test = Test('hello')#会报错
    barget =test.get_bar()
    print(barget) 

if __name__ == "__main__":
    main()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        