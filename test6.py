# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:36:20 2020

@author: Administrator
www.
"""
import requests
#url="http://m.ip138.com/ip.asp?ip="
def findIP(IP):
    url="https://m.ip138.com/iplookup.asp?ip="
    kv={'user-agent':'Mozilla/5.0'}
    #        r=requests.get(url,timeout=30)
    r=requests.get(url+IP,headers=kv)
#    print(r.request.url)
    #print(r.status_code)
    
    r.encoding=r.apparent_encoding
    #print(r.encoding)
#    print(r.text[2469:2480])
    return r.text[2469:2480]
if __name__=="__main__":
    IP=input('please input')
#    IP='52.243.51.215'
    context=findIP(IP)
    print(context)
