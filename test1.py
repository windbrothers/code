# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:00:29 2020

@author: zhyf
简单访问服务器获取连接状态
"""


import requests
r=requests.get('http://www.swfu.edu.cn')
status=r.status_code
#print(status)
#print(r.content)

#r.apparent_encoding
print(r.apparent_encoding)
r.encoding='utf-8'
print(r.text)