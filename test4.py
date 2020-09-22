# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:43:01 2020

@author: Administrator
baidu/360 的搜索API
百度：
http://www.baidu.com/s?wd=keyword
360：
http://www.so.com/s?q=keyword

有问题
"""
import requests
keyword="python"
try:
    kv={'q':keyword}
    r=requests.get("http://www.so.com/s",params=kv)
    
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    print(r.text[1000:2000])
except:
    print('error')
    
