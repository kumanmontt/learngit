# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:24:00 2018

@author: DELL
"""

class Handler:
    '''
    给传入的参数添加一个前缀（start_\end_\sub_）然后返回给method
    查找是否有method这个函数
    如果存在method函数就执行
    '''
    #判断当前类是否有对应的方法，若有的话则根据提供的额外参数使用对应方法
    def callback(self,prefix,name,*args):
        #获取传入参数的值（即prefix+name，函数名）,如果函数名不存在，就返回None
        method = getattr(self,prefix+name,None)
        #如果找得到这个函数，就执行这个函数
        if callable(method):return method(*args)
    
    #callback的辅助方法，给函数提供了start前缀    
    def start(self,name):
        self.callback('start_',name)
        
    def end(self,name):
        self.callback('end_',name)
        
    def sub(self,name):
        #定义substitution函数，该函数将作为re.sub函数的第二个参数
        def substitution(match):#只要进入了这个函数，就表示有匹配的字符串
            #如果有这个函数（sub_name）就返回这个函数
            result = self.callback('sub_',name,match)
            #若callback返回的字符串为空，则返回采用完整的匹配。否则返回回调函数的字符串
            if result is None:result = match.group(0)
            return result
        return substitution
    
    
class HTMLRenderer(Handler):
    '''
    继承自Handler超类函数
    用于生成html的具体处理程序
    HTMLRenderer内的方法都可以通过超类处理程序的start(),end()和sub()方法来访问.他们实现了用于html文档的基本标签
    '''
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
        
    def end_document(self):
        print('</body></html>')
        
    def start_paragraph(self):
        print('<p>')
        
    def end_paragraph(self):
        print('</p>')
        
    def start_heading(self):
        print('<h2>')
        
    def end_heading(self):
        print('</h2>')
        
    def start_list(self):
        print('<ul>')
        
    def end_list(self):
        print('</ul>')
        
    def start_listitem(self):
        print('<li>')
        
    def end_listitem(self):
        print('</li>')
        
    def start_title(self):
        print('<h1>')
        
    def end_title(self):
        print('</h1>')
     
    #斜体（表示强调），找到正则表达式第一个括号对应的匹配字符串
    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)
    #跳转链接
    def sub_url(self,match):
        return '<a href="%s">%s</a>' % (match.group(1),match.group(1))
    #跳转邮箱
    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1),match.group(1))
    #将实际的文本交给程序去处理
    def feed(self,data):
        print (data)
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    