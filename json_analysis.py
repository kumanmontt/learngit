# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:10:15 2018

@author: TAO
"""

import simplejson as json

def json_analysis(data):
    #若数据为列表类型，逐个解析完成也返回列表类型
    if isinstance(data, list):
        return [json_analysis(i) for i in data]
    #若数据为元组类型，逐个解析完成也返回元组类型
    elif isinstance(data, tuple):
        return tuple([json_analysis(i) for i in data])
    #若数据为字典类型，逐个解析完成也返回字典类型
    elif isinstance(data, dict):
        return Storage({json_analysis(k): json_analysis(data[k]) for k in data.keys()})
    else:
        try:
            obj = json.loads(data)
            if obj == data:
                return data
        except:
            return data
        return json_analysis(obj)


class Storage(dict):
    #获取关键字
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)
            
    #修改关键字
    def __setattr__(self, key, value):
        self[key] = value

    #删除关键字
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'