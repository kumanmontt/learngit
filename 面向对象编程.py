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
        
        
#修游泳池
'''
修一个游泳池 半径（以米为单位）在程序运行时输入
游泳池外修一条3米宽的过道，过道的外侧修一圈围墙
已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱（精确到小数点后2位）
'''        
import math

class Circle(object):
    def __init__(self,radius):
        self._radius = radius
        
    @property
    def getradius(self):
        return self._radius
    
    @property
    def setradius(self,radius):
        self._radius = radius if radius >0 else 0
        
    @property
    def perimeter(self):
        return 2*math.pi *self._radius
    
    @property
    def area(self):
        return math.pi *self._radius *self._radius
    
if __name__ == '__main__':
    radius = float(input('请输入游泳池的半径'))
    small = Circle(radius)
    big = Circle(radius+3)
    print('围墙的总造价为￥%.1f'%(big.perimeter*32.5))
    print('过道的总造价为￥%.1f'%((big.area-small.area)*25))
        
        
        
#定义和使用时钟类
import time
import os
class Clock(object):
    #用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
   def __init__(self,**kw):
       if 'hour' in kw and 'minute' in kw and 'second' in kw :
           self._hour = kw['hour']
           self._minute = kw['minute']
           self._second = kw['second']
       else:
           tm = time.localtime(time.time())
           self._hour = tm.tm_hour
           self._minute = tm.tm_min
           self._second = tm.tm_sec
           
   def run(self):
       self._second +=1
       if self._second ==60:
           self._second =0
           self._minute +=1
           if self._minute ==60:
               self._minute =0
               self._hour +=1
               if self._hour ==24:
                   self._hour =0
                  
   def show(self):
       return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)
   
if __name__ == '__main__':
    clock = Clock()
    while True:
        os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()
           
           
#猜数字游戏
from random import randint

class GuessMachine(object):
    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None
        
    def reset(self):
        self._answer = randint(1,100)
        self._counter = 0
        self._hint = None
        
    def guess(self,your_answer):
        self._counter +=1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self.answer:
            self._hint = '大一点'
        else:
            self._hint = '你猜中了'
            return True
        return False
    
    @property
    def counter(self):
        return self._counter
        
    @property
    def hint(self):
        return self._hint
        
if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input("please enter your answer"))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter >7:
            print('you have tried too many times')
        play_again = input('再玩一次？yes/no') == 'yes'
        
        
#定义和使用矩阵类
class Rect(object):  
    def __init__(self,width=0,height=0):
        self.__width = width
        self.__height = height
        
    def perimeter(self):
        '''计算周长'''
        return (self.__width+self.__height)*2
    
    def area(self):
        '''计算面积'''
        return (self.__width * self.__height)
    
    def __str__(self):
        '''矩形对象的字符串表达式'''
        return '矩阵[%f,%f]'%(self.__width,self.__height)
    
    def __del__(self):
        '''构析器'''
        print('销毁矩形对象')
        
if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5,4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
    
    
    
    
'''
python进阶
'''
#property装饰器
class Person(object):
    def __init__(self,name,age):
        self._name =name
        self._age = age
        
    #访问器 getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    
    #修改器 setter方法
    @age.setter
    def age(self,age):
        self._age = age
        
    def play(self):
        if self._age <=16:
            print('%s正在玩飞行棋'%self._name)
        else:
            print('%s正在玩斗地主'%self._name)
            
def main():
    person = Person('wdc',13)
    person.play()
    person.age = 22
    person.play()
    
if __name__ == '__main__':
    main()
        

#__slots__魔法
'''
限定自定义的对象只能绑定某些属性
__slots__的限定只对当前类的对象生效，对子类并不起任何作用
'''
class Person(object):
    #限定Person对象只能绑定_name,_age和_gender属性
    __slots__ = ('_name','_age','_gender')
    def __init__(self,name,age):
        self._name = name
        self._age =age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
        
    def play(self):
        if self._age<19:
            print('%s正在玩飞行器'%self._name)
        else:
            print('%s正在玩斗地主'%self._name)    
            
def main():
    person = Person('WDC',22)
    person.play()
    person.age = 34
    person.play()

if __name__ == '__main__':
     main()
     
#静态方法(staticmethod)
'''
静态方法和类方法都是通过给类发消息来调用的
和类有关系，但是又不会改变类和实例状态的方法
静态方法没有self 和cls参数 可以看成一个普通的函数
'''
from math import sqrt

class Triangle(object):
    def __init__(self,a,b,c):
        self._a =a
        self._b =b
        self._c =c
        
    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c>a and a+c>b
    
    def perimeter(self):
        return self._a +self._b+self._c
    
    def area(self):
        half = self.perimeter()/2
        return sqrt(half *(half -self._a)*(half - self._b)*(half - self._c))
    
def main():
    a,b,c = 3,4,5
    #静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print('无法构成三角形')
        
if __name__ == '__main__':
    main()

#类方法
'''
通过类来调用方法，而不是通过实例
类方法的第一个参数约定名为cls,它代表的是当前类相关的信息的对象
通过这个参数可以获取和类相关的信息并且可以创建出类的对象
'''
from time import time,localtime,sleep
class Clock(object):
    '''数字时钟'''
    def __init__(self,hour=0,minute=0,second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)
    
    def run(self):
        '''走字'''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute +=1
            if self._minute ==60:
                self._minute =0
                self._hour += 1
                if self._hour == 24:
                    self._hour =0
                    
    def show(self):
        '''显示时间'''
        return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)
    
    
def main():
    #通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
        
if __name__ =='__main__':
    main()


#对象之间的依赖关系和运算符重载
class Car(object):
    
    def __init__(self,brand,max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0
        
    @property
    def brand(self):
        return self._brand
    
    def accelerate(self,delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed
            
    def brake(self):
        self._current_speed = 0
        
    def __str__(self):
        return '%s当前时速%d'%(self._brand,self._current_speed)
    
class Student(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    #学生和车之间存在依赖关系 - 学生使用了汽车
    def drive(self,car):
        print('%s驾驶着%s欢快的在去上海的路上'%(self._name,car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        
    def study(self,course_name):
        print('%s正在学习%s'%(self._name,course_name))
        
    def watch(self):
        if self._age <18:
            print('%s观看文学作品'% self._name)
        else:
            print('%s观看史书'%self._name)
    
    # 重载大于（>）运算符
    def __gt__(self,other):
        return self._age >other._age
    
    #重载小于（<）运算符
    def __lt__(self,other):
        return self._age <other._age
    
if __name__ == '__main__':
    stu1 = Student('jully',38)
    stu1.study('Python程序设计')
    stu1.watch()
    stu2 = Student('王大锤',15)
    stu2.study('思想品德')
    stu2.watch()
    car = Car('QQ',120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu2 < stu2)
    
#多重继承
'''
菱形继承（钻石继承）
c3算法（替代DFS的算法）
'''
class A(object):
    
    def foo(self):
        print('foo of A')
        
class B(A):
    pass

class C(A):
    
    def foo(self):
        print('foo of C')#方法重写
        
class D(B,C):
    pass

class E(D):
    
    def foo(self):
        print('foo in E')
        super().foo()#调用父类的方法
        super(B,self).foo()#根据声明顺序，优先查找B类，然后再查找self类
        super(C,self).foo()

if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()


#抽象类/方法重写/多态
'''
实现一个工资结算系统 公司有三种类型的员工
        - 部门经理固定月薪12000元/月
        - 程序员按本月工作小时数每小时100元
        - 销售员1500元/月的底薪加上本月销售额5%的提成
'''
from abc import ABCMeta,abstractmethod

class Employee(object,metaclass=ABCMeta):
    
    def __init__(self,name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        pass
    
class Manager(Employee):
    #构造定义方法
    def __init__(self,name):
        super().__init__(name)
    
    def get_salary(self):  
        return 12000
    
class Programmer(Employee):
    
    def __init__(self,name):
        super().__init__(name)
        
    def set_working_hour(self,working_hour):
        self._working_hour = working_hour
        
    def get_salary(self):
        return 100* self._working_hour
    
class Salesman(Employee):
    
    def __init__(self,name):
        super().__init__(name)
        
    def set_sales(self,sales):
        self._sales = sales
        
    def get_salary(self):
        return 1500 + self._sales * 0.05
    
   
if __name__ == '__main__':
    emps = [Manager('小王'),Programmer('小红'),Salesman('小张')]
    for emp in emps:
        if isinstance(emp,Programmer):
            working_hour = int(input('请输入%s本月的工作时间:'%emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp,Salesman):
            sales = float(input('请输入%s本月的销售额：'%emp.name))
            emp.set_sales(sales)
        print('%s本月的工资为：￥%.2f元'%(emp.name,emp.get_salary()))
        
        
#多重继承
'''
通过多重继承可以给一个类的对象具备多方面的能力
这样在设计类的时候可以避免设计太多层次的复杂的继承关系
'''    
class Father(object):
      
     def __init__(self,name):
         self._name = name
         
     def gamble(self):
         print('%s在打麻将'%self._name)
         
     def eat(self):
         print('%s在大吃大喝'%self._name)
         
class Monk(object):
    
     def __init__(self,name):
         self._name = name
         
     def eat(self):
         print('%s在吃斋'%self._name)
         
     def chant(self):
         print('%s在念经'%self._name)
         
class Musician(object):
    
     def __init__(self,name):
         self._name = name
         
     def eat(self):
         print('%s在细嚼慢咽'%self._name)
         
     def play_paino(self):
         print('%s在弹钢琴'%self._name)
         
class Son(Monk,Father,Musician):
    
    def __init__(self,name):
        Father.__init__(self,name)
        Monk.__init__(self,name)
        Musician.__init__(self,name)
        
son = Son('王大锤')
son.gamble()
son.eat()#按照继承的顺序，如果存在，继承第一个，
son.chant()
son.play_paino()



#运算符重载-自定义分数类
from math import gcd

class Rational(object):
    
    def __init__(self,num,den=1):
        if den ==0:
            raise ValueError('分母不能为0')
        self._num = num
        self._den = den
        self.normalize()
    #化简    
    def simplify(self):
        x = abs(self._num)
        y = abs(self._den)
        factor = gcd(x,y)#取最大公约数
        if factor >1:
            self._num //= factor#num除于最大公约数取整
            self._den //= factor#den除于最大公约数取整
        return self
    
    #除数和被除数都加上一个负号
    def normalize(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num
        return self
    
    def __add__(self,other):
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num,new_den).simplify().normalize()
    
    def __sub__(self,other):
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num,new_den).simplify().normalize()
    
    def __mul__(self,other):
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Rational(new_num,new_den).simplify().normalize()
    
    def __truediv__(self,other):
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Rational(new_num,new_den).simplify().normalize()
    
    def __str__(self):
        if self._num ==0:
            return '0'
        elif self._den ==1:
            return str(self._num)
        else:
            return '(%d/%d)'%(self._num,self._den)

if __name__ == '__main__':
    r1 = Rational(2,3)
    print(r1)
    r2 = Rational(6,-8)
    print(r2)
    print(r1.simplify())
    print('%s + %s = %s'%(r1,r2,r1+r2))
    print('%s - %s = %s'%(r1,r2,r1-r2))    
    print('%s * %s = %s'%(r1,r2,r1*r2))    
    print('%s / %s = %s'%(r1,r2,r1/r2))    




#继承的应用
'''
    -抽象类
    -抽象方法
    -方法重写
    -多态
'''
from abc import ABCMeta,abstractmethod
from math import pi

class Shape(object,metaclass=ABCMeta):
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Rect(Shape):
    
    def __init__(self,width,height):
        self._width = width
        self._height = height
        
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return '我是一个矩形'
    
class Circle(Shape):
    
    def __init__(self,radius):
        self._radius = radius
        
    def perimeter(self):
        return 2 * pi * self._radius
    
    def area(self):
        return pi * self._radius **2
    
    def __str__(str):
        return '我是一个圆'

if __name__ == '__main__':
        shapes = [Circle(5),Circle(3.2),Rect(3.2,6.3)]
        for shape in shapes:
            print(shape)
            print('周长:',shape.perimeter())
            print('面积:',shape.area())


#实例方法和类方法的应用
from math import sqrt

class Triangle(object):
    
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
        
    #静态方法
    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and b + c > a and c + a >b
    
    #实例方法
    def perimeter(self):
        return self._a +self._b +self._c
    
    #实例方法
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p-self._a) * (p - self._b)*(p - self._c))
    
    
if __name__ == '__main__':
    #用字符串的split方法将字符串拆分成一个列表
    #再通过map函数对列表中的每个字符串进行映射处理成小数
    a,b,c = map(float,input('请输入三条边:').split())
    #判断能否构成三角形
    if Triangle.is_valid(a,b,c):
        tri = Triangle(a,b,c)
        print('周长：',tri.perimeter())
        print('面积：',tri.area())
        
    else:
        print('不能构成三角形')
























































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        