# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:26:08 2018

@author: DELL
"""

def lines(file):
    #每次读取一行文件，返回一次line的内容，在文件的最后追加一个空行
    for line in file:yield line
    yield '\n'
  
#依次读取一个文本块
def blocks(file):
    block = []
    for line in lines(file):
        #如果该行文件有值（不为空白行），就去除空格
        if line.strip():
            block.append(line)#把行的内容合并到一起，合并成一个块
        #如果这些行合并完了（整个段落的内容都提取到一起了）成为了一个块
        elif block:
            yield ''.join(block).strip()#把块的内容提取出来
            block = []#然后block置空（等待下一次函数的调用，可以读取读取下一个块）