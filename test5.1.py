# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:31:23 2020

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup
def getContent(url):
    try:
        #kv={'user-agent':'Mozilla/5.0'}
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        r.raise_for_status
        print(r.status_code)
#        print(r.request.headers)
        return r.text
    except:
        return 'error'
if __name__=="__main__":
    url="http://python123.io/ws/demo.html"
    demo=getContent(url)
#    print(demo)
    soup=BeautifulSoup(demo,"html.parser")
#    t=soup.title 
#    b=soup.body
    a=soup.a
#    #标签名字
#    name=soup.a.name
#    name=soup.a.parent.parent.parent.name
##    标签属性
    tag=a.attrs
#
#    tag=tag['href']
#    keyattrs=type(a.attrs)
#    p=soup.p 
#    #获取标签内容
#    string=p.string
    string=a.attrs['href']
    print(string)
#    print(soup.attrs)
#    print(type(p.string))
#    print(soup.prettify())
#    print(demo)
