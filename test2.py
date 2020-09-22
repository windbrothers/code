# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:16:05 2020

@author: Administrator
代码框架
小规模爬虫用requests库
中等规模的用Scrapy库

"""
import requests

def getHTMLTest(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()# 网络连接的异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '出现异常'

if __name__=="__main__":
    url="http://www.baidu.com"
#    url="http://www.swfu.edu.cn"
    url="https://www.booktxt.net/2_3257/"
#    url="https://www.booktxt.net/2_3257/1214837.html"
    print(getHTMLTest(url))
