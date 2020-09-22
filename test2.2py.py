# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:41:59 2020
@author: Administrator
遍历标签
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
#    1树形遍历
    demo=getContent(url)
#    print(demo)
    soup=BeautifulSoup(demo,"html.parser")
    print(soup.body.prettify())
#    print(soup.prettify())
#    h=soup.head
##    print(soup.head)
##    print(soup.contents)
#    b=soup.body
##    print(b)
##    print('****')
##    print(b.contents)
#    print(len(b))
#    print(b.contents[1])
#    parent=soup.title.parent
#    print(parent)
#    遍历先辈信息
#    for parent in soup.a.parents:
#        if parent is None:
#            print(parent)
#        else:
#            print(parent.name)
#    2平行遍历
#    for sibling in soup.a.next_siblings:
#        print(sibling)
#            
#    for sibling in soup.a.previous_siblings:
#        print(sibling)
    
