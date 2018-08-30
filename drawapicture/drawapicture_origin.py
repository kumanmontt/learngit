# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 18:51:36 2018

@author: DELL
"""

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF


data = [
        #year month predicted high low
        (2007,8,113.2,114.2,112.2),
        (2007,9,112.8,115.8,109.8),
        (2007,10,111.0,116.0,106.0),
        (2007,11,109.8,116.8,102.8),
        (2007,12,107.3,115.3,99.3),
        (2008,1,105.2,114.2,96.2),
        (2008,2,104.1,114.1,94.1),
        (2008,3,99.9,110.9,88.9),
        (2008,4,94.8,106.8,82.8),
        (2008,5,91.2,104.2,78.2),
       
        ]

drawing = Drawing(200,150)#画背景
pred = [row[2]-40 for row in data]#每个元组的第二个值
high = [row[3]-40 for row in data]#每个元组的第三个值
low = [row[4]-40 for row in data]#每个元组的第四个值
times = [200*((row[0] + row[1]/12.0) -2007)-110 for row in data]

drawing.add(PolyLine(list(zip(times,pred)),strokeColor=colors.blue))#把time和Pred结合起来画图
drawing.add(PolyLine(list(zip(times,high)),strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times,low)),strokeColor=colors.green))
drawing.add(String(65,115,'Sunspots',fontSize=18,fillColor=colors.red))#设置文字

renderPDF.drawToFile(drawing,'report.pdf','Sunspots')#保存文件的名称和pdf的名称






















