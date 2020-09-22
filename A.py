# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:22:01 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:03:27 2020

@author: zhyf
E-mail:zhyfwcy@gmail.com

说明：

"""
import os
from PIL import Image
from pyzbar import pyzbar
import cv2 as cv
import numpy as np
import math 
import random
def shengchengshuju(ID,y0,y1,x0,x1,image):
    name='./cut1/'
    X=random.randint(1,10000000)
    num=1
    savename=name+str(X)+str(num)+'_'+str(ID)+'.jpg'
    

    K=3
    X_L=int((abs(x0-x1)/2)/K)
    Y_L=int((abs(y0-y1)/2)/K)
    center_point_x=int(abs(x0+x1)/2)
    center_point_y=int(abs(y0+y1)/2)
    y0=int(center_point_y-Y_L)
    y1=int(center_point_y+Y_L)
    x0=int(center_point_x-X_L)
    x1=int(center_point_x+X_L)


    cropped = image[y0:y1,x0:x1]
    cropped=cv.resize(cropped,(400,300))
    cv.imwrite(savename,cropped)
    num=num+1
    print(y0,y1,x0,x1)


def decode_qr_code(path,filename):
    Mask=cv.imread(path)
    print(Mask.shape)
    h=int(Mask.shape[0]/3)
    w=int(Mask.shape[1]/3)
    print(w,h)
#    Mask=cv.resize(Mask,(400,300))
    Mask=cv.resize(Mask,(600,450))
#    Mask=cv.resize(Mask,(1200,900))

    return 1,Mask
def bianji(image,photoName):
#    image = image.resize((400, 300))

    info=[]
    ID=0
    H=image.shape[0]
    W=image.shape[1]
#外边框
    h=H/100  #3
    w=W/100  #4
#    cv.rectangle(image,(0,0),(W,H),(255,0,0),2)
    #标题 品种
#    cv.rectangle(image,(35,0),(240,H1),(0,255,0),2)
#1后备发情
    #标题 次数
#    H1=int(h*5)
#    H2=int(h*9)
#    W1=int(w*18)
#    W2=int(w*61)
#    cv.rectangle(image,(W1,H1),(W2,H2),(0,255,0),2)

##切割
    1
    H3=int(h*10)
    H4=int(h*13)     
#    cv.rectangle(image,(W1,H4),(W2,H3),(0,0,255),2)
    
    A1=int(w*18)
    w1=7*h
    for i in range(2):
        x0=int(w1*(i)+A1)
        x1=int(w1*(i+1)+A1)
        y0=H3
        y1=H4
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A2=int(w*34)
    for i in range(2):
        x0=int(w1*(i)+A2)
        x1=int(w1*(i+1)+A2)
        y0=H3
        y1=H4
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*50)
    for i in range(2):
        x0=int(w1*(i)+A3)
        x1=int(w1*(i+1)+A3)
        y0=H3
        y1=H4
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    
    #2
    H5=int(h*15)
    H6=int(h*18)
#    cv.rectangle(image,(W1,H5),(W2,H6),(0,0,255),2)
    A1=int(w*18)
    w1=7*h
    for i in range(2):
        x0=int(w1*(i)+A1)
        x1=int(w1*(i+1)+A1)
        y0=H5
        y1=H6
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A2=int(w*34)
    for i in range(2):
        x0=int(w1*(i)+A2)
        x1=int(w1*(i+1)+A2)
        y0=H5
        y1=H6
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*50)
    for i in range(2):
        x0=int(w1*(i)+A3)
        x1=int(w1*(i+1)+A3)
        y0=H5
        y1=H6
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    
##2二维码
    HH=int(h*50)    #24
#    cv.rectangle(image,(0,H6),(W2,HH),(0,0,255),2)
    w2=int(31*w)
    A3=int(0)
    for i in range(2):
        x0=int(w2*(i)+A3)
        x1=int(w2*(i+1)+A3)
        y0=H6
        y1=HH
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

##3胎次
    #标题 胎次 间隔
#    H7=int(h*50) 
#    H8=int(h*53)
#    cv.rectangle(image,(0,H7),(W2,H8),(0,255,0),2)
    #1
    H9=int(h*54.5) 
    H10=int(h*57.5) 
#    cv.rectangle(image,(0,H9),(W2,H10),(0,0,255),2)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    #2
    H9=int(h*59)
    H10=int(h*62)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    
#    #3
    H9=int(h*63.5)
    H10=int(h*66.5)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

#    #4
    H9=int(h*68)
    H10=int(h*71)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    
#    #5
    H9=int(h*72.5)
    H10=int(h*75)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#4免疫
#    #1
    w3=int(4.8*w)
    H10=int(h*83)
    H11=int(h*86)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)        
#    2
    H10=int(h*88)
    H11=int(h*91)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID) 
#    #3
    H10=int(h*92.5)
    H11=int(h*95.5)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID) 
#    #4
    H10=int(h*97)
    H11=int(h*100)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    
#5背标
    #标题 配种前
#    #1
    w4=int(5*w)
    H10=int(h*83)
    H11=int(h*86)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#    2
    H10=int(h*88)
    H11=int(h*91)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#    #3
    H10=int(h*92.5)
    H11=int(h*95.5)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#    #4
    w4=int(5*w)
    H10=int(h*97)
    H11=int(h*100)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
 #6顺产、助产
    w4=int(12*w)
    H14=int(h*72)
    H13=int(h*75)
    H11=int(h*100)
    A3=int(w*76)
    for i in range(1):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H14
        y1=H13
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*89)
    for i in range(1):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H14
        y1=H13
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
        
# 7 返情
##    1
    H13=int(h*24)
    H14=int(h*27)
    w7=int(6.0*w)
    A7=int(w*81)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
###    2
    H13=int(h*28)
    H14=int(h*31)

    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
        print(x0,x1,y0,y1)
        print(ID)
###    3
    H13=int(h*32)
    H14=int(h*35)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
####    4
    H13=int(h*37)
    H14=int(h*40)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
##    #5
    H13=int(h*41.5)
    H14=int(h*44)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
###    6
    H13=int(h*45)
    H14=int(h*48)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
##    #7
    H13=int(h*49.5)
    H14=int(h*52.5)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
##    #8
    H13=int(h*54)
    H14=int(h*57)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
##    #9
    H13=int(h*59)
    H14=int(h*62)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
##    #10
    H13=int(h*64)
    H14=int(h*67)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H13
        y1=H14
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#8配种人
    #1
    H15=int(h*10)
    H16=int(h*13)
    w8=int(w*4)
    A8=int(w*62)
    for i in range(2):
        x0=int(w8*(i)+A8)
        x1=int(w8*(i+1)+A8)
        y0=H15
        y1=H16
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    #2
    H15=int(h*15)
    H16=int(h*18)
    for i in range(2):
        x0=int(w8*(i)+A8)
        x1=int(w8*(i+1)+A8)
        y0=H15
        y1=H16
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#8配种评分
    #1
    H17=int(h*5.5)
    H18=int(h*8.5)
    w9=int(w*5.5)
    A8=int(w*73.5)
    for i in range(3):
        x0=int(w9*(i)+A8)
        x1=int(w9*(i+1)+A8)
        y0=H17
        y1=H18
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    #2
    H17=int(h*10)
    H18=int(h*13)
    for i in range(3):
        x0=int(w9*(i)+A8)
        x1=int(w9*(i+1)+A8)
        y0=H17
        y1=H18
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
#    #3
    H17=int(h*15)
    H18=int(h*18)
    for i in range(3):
        x0=int(w9*(i)+A8)
        x1=int(w9*(i+1)+A8)
        y0=H17
        y1=H18
#        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
#        print(x0,x1,y0,y1)
        print(ID)
    image=cv.resize(image,(1200,900))
    cv.imwrite('./ReSize/'+filename,image)
if __name__ == '__main__':
        Sum =0
        filepath='./cut/'
        for filename in os.listdir(filepath):
            path = filepath+filename
            
            x,mask=decode_qr_code(path,filename)
            bianji(mask,filename)
            Sum=Sum+x
        print('识别成功的二维码张数',Sum)
        
#                Orig_url = filepath+filename
#                url.append(Orig_url)
#        #        print(Orig_url)
#                photoName=Orig_url.split("/")[-1]
##                name.append(photoName)
#        print('照片总张数',len(name))# 