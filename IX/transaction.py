#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问OKCOIN 期货REST API
from httpsha256Util import buildMySign,httpGet,httpPost

class IXquot:

    def __init__(self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey

    #期货全仓持仓信息
    def account(self,symbol,contractType):
        FUTURE_POSITION = "/api/v1/future_position.do?"
        params = {
            'api_key':self.__apikey,
            'symbol':symbol,
            'contract_type':contractType
        }
        params['sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_POSITION,params)