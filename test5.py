# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:55:17 2020

@author: Administrator
爬取照片框架
"""

import requests
import os
root="D://down1//"
url="http://139.9.114.227/1.jpg"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        print(r.status_code)
        r.raise_for_status()# 网络连接的异常
        with open (path,'wb') as f:
            f.write(r.content)
            f.close
        print('文件下载成功')
    else:
        print("文件已存在")
except:
    print('文件下载失败')