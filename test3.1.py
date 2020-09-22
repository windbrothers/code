# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:30:57 2020

@author: Administrator
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:16:05 2020

@author: Administrator
代码框架
小规模爬虫用requests库
中等规模的用Scrapy库

"""
import requests
from bs4 import BeautifulSoup
import re
def getHTMLTest(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()# 网络连接的异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '出现异常'

if __name__=="__main__":
#    url="http://www.baidu.com"
#    url="http://www.swfu.edu.cn"
    url="https://www.booktxt.net/2_3257/"
#    url="https://www.booktxt.net/2_3257/1214837.html"
    con=[]
    demo=getHTMLTest(url)
    soup=BeautifulSoup(demo,'html.parser')
    print(soup)
#    context_f=soup.find_all('a')
#    context_f=soup.find_all(['dd' ])
#    print(context_f)
    context_f=soup.find_all(string=re.compile('超级通灵系统'))
    print(context_f)
#    for tag in soup.find_all(True):
#        print(tag.name  )

