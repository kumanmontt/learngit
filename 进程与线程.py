# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:07:42 2018

@author: DELL
"""


'''
#不使用多进程
from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()



#使用多进程
from  multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].'%getpid())
    print('开始下载%s...'%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒'%(filename,time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task,args=('python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task,args=('Pndjenjnn.xlx',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.'%(end - start))

if __name__ == '__main__':
    main()



#thread模块对多线程编程提供了更好的面向对象的封装
from random import randint
from threading import Thread
from time import time,sleep
def download(filename):
    print('开始下载%s...'%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒'%(filename,time_to_download))

def main():
    start = time()
    t1 = Thread(target=download,args=('python丛书没人能.pdf',))
    t1.start()
    t2 = Thread(target=download,args=('hgueeuich.xlx',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒'%(end - start))

if __name__ == '__main__':
    main()



#继承Thread类的方式来创建自定义的线程类，然后创建线程对象并启动线程
from random import randint
from threading import Thread
from time import time ,sleep

class DownloadTask(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...'%self._filename)
        time_to_download = randint(5,10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒'%(self._filename,time_to_download))

def main():
    start = time()
    t1 = DownloadTask('PytonNNIK.pdf')
    t1.start()
    t2 = DownloadTask('njciowji.xlzx')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒。'%(end-start))

if __name__ == '__main__':
    main()






#通过锁来保护临界资源，只有获得锁的线程才能访问临界资源
#没有得到锁的线程只能被阻塞起来，直到获得锁的线程释放了锁，其他线程才有机会获得锁，进而访问临界资源

from time import sleep
from threading import Thread,Lock
class Account(object):
    def __init__(self):
        self._balance =0
        self._lock = Lock()

    def deposit(self,money):
        #先获得锁才能执行后续代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance#更新值
        finally:
            #在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()
    @property
    def balance(self):
        return self._balance


class ADDMoneyThread(Thread):

    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = ADDMoneyThread(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：￥%d元'%account.balance)


if __name__ == '__main__':
    main()


'''
#将耗时间的任务放到线程中以获得更好的用户体验
import time
import tkinter
import tkinter.messagebox
def download():
   #模拟下载任务需要花费10秒钟时间
   time.sleep(10)
   tkinter.messagebox.showinfo('提示','下载完成！')#显示模拟对话框

def show_about():
    tkinter.messagebox.showinfo('关于','作者：骆昊(V1.0)')

def main():
    top = tkinter.TK()#初始化TK()
    top.title('单线程')
    top.geometry('200*150')#设置窗口大小
    top.wm_attributes('-topmost',True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text='下载',command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='关于',command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()

if __name__ == '__main__':
    main()



















