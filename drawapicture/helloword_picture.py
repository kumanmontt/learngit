# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 18:21:27 2018

@author: DELL
"""

from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)#设置画布大小
s = String(50,50,'hello,world!',textAnchor = 'middle')#设置内容，格式

d.add(s)#画布上添加内容

renderPDF.drawToFile(d,'hello.pdf','A simple PDF file')#生成文件