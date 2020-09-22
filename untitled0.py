# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:39:28 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:41:32 2020

@author: Administrator
小说爬取 ：http://www.biquge.se/1791/
"""

import requests
from bs4 import BeautifulSoup
import bs4
import re
import os
def getHTMLTest(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()# 网络连接的异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '出现异常'
def findURL_Contlist(ulist,html,url):
    soup=BeautifulSoup(html,'html.parser')
    print(soup)
    for a in soup.find_all('dd'):
        if isinstance(a,bs4.element.Tag):
            context_title=a.string
            a=str(a)
            print('a的值',a)
            url_c=a.split('"')[-2]
            print('章节',context_title)
            context_url=url+url_c
            print('url',context_url)
            ulist.append([context_title,context_url])
    return ulist

def getcontext(title,url):
    print('title','url',title,url)
#    title='我不够资格1'
    path=root+title+'.txt'
    print(path)
    if not os.path.exists(root):
        os.mkdir(root)
    else:
        if not os.path.exists(path):
            f=open(path, "a+")
            con=[]
            context_ok=[]
#            url='http://www.biquge.se/1791/73990790.html'
#            url='http://www.biquge.se/1791/74030486.html'
            print(url)
            html=getHTMLTest(url)
            soup=BeautifulSoup(html,'html.parser')
            context=soup.div
            for i in context:
                con.append(i)
            d_context=str(con[7])
            d_context=str(d_context.split('</script>')[3:-2])
            context=d_context.split('<br/>')
            for i in context:
                context_ok.append(i)
            for i in range(len(context_ok)-1):
                if(i==0):
                    f.write(title)
                else:
                    word=str(context_ok[i])
                    dword=re.sub(r'\\u3000','', word)
                   
                    dword=re.sub(r'\\xa0','', dword)
                    f.write('\n'+dword)
            f.close()
            print('{}写入完成'.format(title))
#        else:
#            print('{}章节已存在'.format(title))
def printViewlist(ulist,num):
#    tplt="{0:^10}\t{1:^10}"
#    print(tplt.format("章节","链接"),chr(12288))
    for i in range(num):
        u=ulist[i]
#        print(tplt.format(u[0],u[1],),chr(12288))
        print('{}张正在写入'.format(i+1))
        getcontext(str(u[0]),str(u[1]))

if __name__=="__main__":
#    url="http://www.biquge.se/1791/"
    url="https://www.booktxt.net/2_3257/"
    root="D://最强医圣1/"
    uinfo=[]
    html=getHTMLTest(url)
    cont_list=findURL_Contlist(uinfo,html,url)
    num=int(len(cont_list)-8)
    printViewlist(uinfo,num)



