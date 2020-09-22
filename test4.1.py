# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:55:35 2020

@author: Administrator
url=http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html
爬取大学排名
"""
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLTest(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()# 网络连接的异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '出现异常'
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,
                          tds[1].string,
                          tds[2].string])
    pass
def printUnivlist(ulist,num):
    tplt="{0:^2}\t{1:^10}\t{2:^4}"
    print(tplt.format("排名","学校名称","地区"),chr(12288))
    for i in range(num):
        u=ulist[i]
#        print(len(u)) 
        if(u[2]=='云南'):
                print(tplt.format(u[0],u[1],u[2]),chr(12288))

#        print(tplt.format(u[0],u[1],u[2]),chr(12288))

if __name__=="__main__":
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html"
    uinfo=[]
    html=getHTMLTest(url)
#     
    fillUnivList(uinfo,html)
    printUnivlist(uinfo,560)
#    printUnivlist(uinfo,num)
#    print(soup)

