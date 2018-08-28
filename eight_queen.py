# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:17:32 2018

@author: DELL
"""
import random
def conflict(state,nextx):
    #state是已有皇后位置的元组，nextx是下一个皇后的水平位置，nexty是下一个皇后的垂直位置
    nexty = len(state)
    for i in range(nexty):#排除了在同一行的情况
        if abs(state[i]-nextx) in (0,nexty-i):
            '''
            if (state[i]-nextx)==0:说明在同一列
            if (state[i]-nextx)==nexty-i:说明行数之差和列数之差相等，会形成对角线
            '''
            return True
    return False

def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):#如果位置不冲突
            if len(state) == num -1:#如果是最后一个皇后
                yield (pos,)#返回该位置
            else:#如果不是最后一个皇后。就把该位置返回到state元组，并且传给后面的皇后
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result

def prettyp(solution):
    #打印函数
    def line(pos,length = len(solution)):#打印一行，皇后的位置用X填充，其余用0填充
        return 'O'*(pos)+'X'+'O'*(length-pos-1)
    
    for pos in solution:#打印所有行
        print(line(pos))
        
prettyp(random.choice(list(queens(8))))#随机打印一种皇后的情况