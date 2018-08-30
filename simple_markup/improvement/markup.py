# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:54:12 2018

@author: DELL
"""

import sys,re
#sys.path.append("..")
from handlers import *
from util import *
from rules import*
class Parser:
    '''
    语法分析器读取文本文件、应用规则、并且控制处理程序
    '''
    def __init__(self,handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    #把规则添加到规则列表
    def addRule(self,rule):
        self.rules.append(rule)
    #将过滤器添加到第一个过滤器
    def addFilter(self,pattern,name):
        #先创建一个过滤器，用已经定义的函数名替换原来的值
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    #读取文本文件，循环出每一个文本块，先通过过滤器，然后执行相应规则
    def parse(self,file):
        self.handler.start('document')
        #对文件中的文本依次执行过滤器和规则
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last:break
        self.handler.end('document')
            

class BasicTextParser(Parser):
    '''
    在构造函数中增加规则和过滤器的具体语法分析器
    '''
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        
        self.addFilter(r'\*(.+?)\*' , 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')
#初始化类，并且对文件执行parse方法，即时标记项目完成        
handler = HTMLRenderer()
parser = BasicTextParser(handler)


parser.parse(sys.stdin)
        
                    