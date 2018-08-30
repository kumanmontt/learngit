# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:21:23 2018

@author: DELL
"""

class Rule:
    '''
    所有规则的基类
    '''
    def action(self,block,handler):
        handler.start(self.type)#添加标签起始标记
        handler.feed(block)#然后处理字符串
        handler.end(self.type)#最后添加标签结束标记
        return True
    
    
class HeadingRule(Rule):
    type = 'heading'
    #每一个规则的子类，都应该有condition函数，用来判断当前字符串是否符合子类规则
    def condition(self,block):
        #string中没有换行符，且string长度小于等于70，且字符串的最后一个字符不等于‘：’
        #满足以上条件，该字符串为标题
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'
    
    
class TitleRule(HeadingRule):
    '''
    题目是文档的第一个块，但前提是他是大标题，继承HeadingRule()函数
    '''
    type = 'title'
    first = True
    
    def condition(self,block):
        if not self.first:return False#确保是第一个块
        self.first = False
        return HeadingRule.condition(self,block)
    
    
class ListItemRule(Rule):
    '''
    列表项是以字符开始的段落，作为格式化的一部分，要移除连字符
    '''
    type = 'listitem'
    def condition(self,block):#如果第一个字符是"-"就返回False
        return block[0] == '-'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())#移除第一个字符串(从第二个字符开始)
        handler.end(self.type)
        return True
    
    
class ListRule(ListItemRule):
    '''
    列表从不是列表项的块和随后的列表项之间。在最后一个连续列表项之后结束
    '''
    type = 'list'
    inside = False
    def condition(self,block):
        return True
    def action(self,block,handler):
        #（inside特性指出分析器是否在列表中）inside特性是假以及来自列表项规则的条件是真，进入了一个列表
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            self.inside = True
        #离开了列表
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside = False
        return False
    
    
class ParagraphRule(Rule):
    '''
    段落只是其他规则没有覆盖到的块
    '''
    type = 'paragraph'
    def condition(self,block):
        return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    