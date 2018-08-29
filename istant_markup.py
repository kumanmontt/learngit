# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:49:00 2018

@author: TJD
"""
'''
文件运行代码为python istant_markup.py <test_input.txt> test_output.html
'''
import sys,re
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



print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    #正则表达式的替换，非贪婪匹配**之前的内容，并且给他加上一个em标签（斜线表示，起强调作用）
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    #第一段读进来的文字给他加上<h>标签表示是文章的标题
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    #其他读进来的加上<p>标签表示是文章的段落
    else:
        print('<p>')
        print(block)
        print('</p>')
        
print('</body></html>')

