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
def decode_qr_code(path,filename):
    Mask=cv.imread(path)
    print(Mask.shape)
    h=int(Mask.shape[0]/3)
    w=int(Mask.shape[1]/3)
    print(w,h)
#    Mask=cv.resize(Mask,(400,300))
    Mask=cv.resize(Mask,(1200,900))

    return 1,Mask
#        for j in range(len(X)):
#               y0=y-1
#               y1=y+1
#               x0=X[j]-2
#               x1=X[j]+2
##               cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#               ID=ID+1
##               info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
def shengchengshuju(ID,y0,y1,x0,x1,image):
    y0=y0+5
    y1=y1-5
    x0=x0+5
    x1=x1-5
    ptStart = (x0, y0)
    ptEnd = (x1, y1)
    ptStart1 = (x0, y1)
    ptEnd1 = (x1, y0)


    cropped = image[y0:y1,x0:x1]
#    w=int(cropped.shape[0]/5)
#    h=int(cropped.shape[1]/5)
#    print(w,h)
#
#    cropped=cv.resize(cropped,(w,h))
    hsv = cv.cvtColor(cropped, cv.COLOR_BGR2HSV)
    low_hsv = np.array([0,153,35])
    high_hsv = np.array([180,255,255])
##    红色
#    low_hsv = np.array([0,43,46])
#    high_hsv = np.array([10,255,255])

    Mask = cv.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
    dilation = cv.dilate(Mask,np.ones((5,5),np.uint8),iterations = 1)
    Mask = cv.erode(dilation,np.ones((3,3),np.uint8),iterations = 1)



    pint_W=Mask.shape[0]-1
    pint_H=Mask.shape[1]-1
#    print(ID,'长度及宽度',pint_W,pint_H)
    area=(pint_W+1)*(pint_H+1)
    Wk=0#Wk 白色
    Bk=0#Bk 黑色
    for i in range(pint_W):
        for j in range(pint_H):
            if(Mask[i][j]==255):
#                print(Mask[pint_W][pint_H])
                Wk=Wk+1
            elif(Mask[i][j]==0):
#                print(Mask[pint_W][pint_H])
                Bk=Bk+1
            else:
                print('error!')
#                print(Mask[pint_W][pint_H])

#    if not os.path.exists('./ceshijubu/'):
#        os.makedirs('./ceshijubu/')
#    num=str(ID)
#    juquname='./ceshijubu/'+num+'.jpg'
#    cv.imwrite(juquname,Mask)
    R=Wk/area
    if(R>0.5151515151):
        cv.line(image, ptStart, ptEnd, (0, 255, 0), 1, 4)
        cv.line(image, ptStart1, ptEnd1, (0, 255, 0), 1, 4)
        sign=1
    else:
        sign=0
    cv.waitKey()
    return sign


def bianji(image,photoName):
#    image = image.resize((400, 300))

    info=[]
    ID=0
    H=image.shape[0]
    W=image.shape[1]
#外边框
    h=H/100  #3
    w=W/100  #4
    cv.rectangle(image,(0,0),(W,H),(255,0,0),2)
    #标题 品种
#    cv.rectangle(image,(35,0),(240,H1),(0,255,0),2)
#1后备发情
    #标题 次数
    H1=int(h*5)
    H2=int(h*9)

#    W1=int(w*13)
#    W2=int(w*61)
    
    W1=int(w*18)
    W2=int(w*61)
    cv.rectangle(image,(W1,H1),(W2,H2),(0,255,0),2)

##切割

#           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#           info.append(info_array)
#           print(info)
#           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#           x0=x1=y0=y1=0


    #1
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
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A2=int(w*34)
    for i in range(2):
        x0=int(w1*(i)+A2)
        x1=int(w1*(i+1)+A2)
        y0=H3
        y1=H4
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*50)
    for i in range(2):
        x0=int(w1*(i)+A3)
        x1=int(w1*(i+1)+A3)
        y0=H3
        y1=H4
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
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
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A2=int(w*34)
    for i in range(2):
        x0=int(w1*(i)+A2)
        x1=int(w1*(i+1)+A2)
        y0=H5
        y1=H6
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*50)
    for i in range(2):
        x0=int(w1*(i)+A3)
        x1=int(w1*(i+1)+A3)
        y0=H5
        y1=H6
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
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
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
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
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #2
#    H11=int(h*59)
#    H12=int(h*62)
#    cv.rectangle(image,(0,H11),(W2,H12),(0,0,255),2)
    H9=int(h*59)
    H10=int(h*62)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
#    #3
#    H13=int(h*63.5)
#    H14=int(h*66.5)
#    cv.rectangle(image,(0,H13),(W2,H14),(0,0,255),2)
    H9=int(h*63.5)
    H10=int(h*66.5)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

#    #4
#    H15=int(h*68)
#    H16=int(h*71)
#    cv.rectangle(image,(0,H15),(W2,H16),(0,0,255),2)
#    H15=int(h*68)
#    H16=int(h*71)

    H9=int(h*68)
    H10=int(h*71)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
#    #5
#    H17=int(h*72.5)
#    H18=int(h*75)
#    cv.rectangle(image,(0,H17),(W2,H18),(0,0,255),2)
    
    H9=int(h*72.5)
    H10=int(h*75)
    w3=int(5*w)
    A3=int(0)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(15.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)

    A3=int(31*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(46.5*w)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H9
        y1=H10
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#4免疫
    #标题 胎次
#    H18=int(h*75)
#    HH1=int(h*82) 
#    W3=int(w*14)
#    W4=int(w*63)
#    cv.rectangle(image,(W3,HH1),(W4,H18),(0,255,0),2)
#    #1
    w3=int(4.8*w)

#    H19=int(h*83)
#    H20=int(h*86)
#    cv.rectangle(image,(W3,H19),(W4,H20),(0,0,255),2)
    
    H10=int(h*83)
    H11=int(h*86)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)        
        
#    2
#    H21=int(h*88)
#    H22=int(h*91)
#    cv.rectangle(image,(W3,H21),(W4,H22),(0,0,255),2)
    H10=int(h*88)
    H11=int(h*91)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID) 
#    #3
#    H23=int(h*92.5)
#    H24=int(h*95.5)
#    cv.rectangle(image,(W3,H23),(W4,H24),(0,0,255),2)
    
    H10=int(h*92.5)
    H11=int(h*95.5)

    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID) 
#    #4
#    H25=int(h*97)
#    H26=int(h*100)
#    cv.rectangle(image,(W3,H25),(W4,H26),(0,0,255),2)
    H10=int(h*97)
    H11=int(h*100)
    A3=int(w*14)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*29)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*38.5)
    for i in range(3):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*53)
    for i in range(2):
        x0=int(w3*(i)+A3)
        x1=int(w3*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
#5背标
    #标题 配种前
#    HH1=int(h*82) 
    W5=int(w*64.5)
    W6=int(w*90.5)
    
    
#    cv.rectangle(image,(W5,HH1),(W6,H18),(0,255,0),2)
    
    
#    #1
#    H19=int(h*83)
#    H20=int(h*86)
#    cv.rectangle(image,(W5,H19),(W6,H20),(0,0,255),2)
    
    
    w4=int(5*w)
    H10=int(h*83)
    H11=int(h*86)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
#    2
#    H21=int(h*88)
#    H22=int(h*91)
#    cv.rectangle(image,(W5,H21),(W6,H22),(0,0,255),2)
    H10=int(h*88)
    H11=int(h*91)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#    #3
#    H23=int(h*92.5)
#    H24=int(h*95.5)
#    cv.rectangle(image,(W5,H23),(W6,H24),(0,0,255),2)
    H10=int(h*92.5)
    H11=int(h*95.5)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#    #4
#    H25=int(h*97)
#    H26=int(h*100)
#    cv.rectangle(image,(W5,H25),(W6,H26),(0,0,255),2)
    w4=int(5*w)
    H10=int(h*97)
    H11=int(h*100)
    A3=int(w*64.5)
    for i in range(5):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H10
        y1=H11
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
    
 #6顺产、助产
#    HH2=int(h*72)
#    HH3=int(h*67)
    
    W7=int(w*77)
    W8=int(w*100)
#    cv.rectangle(image,(W7,HH2),(W8,HH3),(0,255,0),2)
#    H01=int(h*72)
#    H00=int(h*75)
#    cv.rectangle(image,(W7,H01),(W8,H00),(0,0,255),2)
    
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
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    A3=int(w*89)
    for i in range(1):
        x0=int(w4*(i)+A3)
        x1=int(w4*(i+1)+A3)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#    1
#7返情
    #标题 返情

    W7=int(w*81)
    W8=int(w*100)
#    cv.rectangle(image,(W7,HH2),(W8,HH3),(0,255,0),2)
    
    
    
##    #1
#    H27=int(h*24)
#    H28=int(h*27)
#    cv.rectangle(image,(W7,H27),(W8,H28),(0,0,255),2)
    H14=int(h*24)
    H13=int(h*27)
    w7=int(6.5*w)
    
    A7=int(w*81)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
##    2
    H13=int(h*28)
    H14=int(h*31)
#    cv.rectangle(image,(W7,H29),(W8,H30),(0,0,255),2)

    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
##    3
#    H13=int(h*32)
#    H14=int(h*35)
#    cv.rectangle(image,(W7,H31),(W8,H32),(0,0,255),2)
    H13=int(h*32)
    H14=int(h*35)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
##    4
#    H33=int(h*37)
#    H34=int(h*40)
#    cv.rectangle(image,(W7,H33),(W8,H34),(0,0,255),2)
    H13=int(h*37)
    H14=int(h*40)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    
    #5
#    H35=int(h*41.5)
#    H36=int(h*44)
#    cv.rectangle(image,(W7,H35),(W8,H36),(0,0,255),2)
    H13=int(h*41.5)
    H14=int(h*44)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#    6
#    H37=int(h*45)
#    H38=int(h*48)
#    cv.rectangle(image,(W7,H37),(W8,H38),(0,0,255),2)
    H13=int(h*45)
    H14=int(h*48)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #7
#    H39=int(h*49.5)
#    H40=int(h*52.5)
#    cv.rectangle(image,(W7,H39),(W8,H40),(0,0,255),2)
    H13=int(h*49.5)
    H14=int(h*52.5)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #8
#    H41=int(h*54)
#    H42=int(h*57)
#    cv.rectangle(image,(W7,H41),(W8,H42),(0,0,255),2)
    H13=int(h*54)
    H14=int(h*57)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #9
#    H43=int(h*59)
#    H44=int(h*62)
#    cv.rectangle(image,(W7,H43),(W8,H44),(0,0,255),2)
    H13=int(h*59)
    H14=int(h*62)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #10
#    H45=int(h*64)
#    H46=int(h*67)
#    cv.rectangle(image,(W7,H45),(W8,H46),(0,0,255),2)
    H13=int(h*64)
    H14=int(h*67)
    for i in range(3):
        x0=int(w7*(i)+A7)
        x1=int(w7*(i+1)+A7)
        y0=H14
        y1=H13
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#8配种人
    #标题 次数
    H1=int(h*5)
    H2=int(h*9)
#    W1=int(w*9)
#    W9=int(w*61)
#    W10=int(w*72)
#    cv.rectangle(image,(W9,H1),(W10,H2),(0,255,0),2)
    #1
#    H3=int(h*10)
#    H4=int(h*13)
#    cv.rectangle(image,(W9,H4),(W10,H3),(0,0,255),2)
    H15=int(h*10)
    H16=int(h*13)
    w8=int(w*4)
    A8=int(w*62)
    for i in range(2):
        x0=int(w8*(i)+A8)
        x1=int(w8*(i+1)+A8)
        y0=H15
        y1=H16
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #2
    H15=int(h*15)
    H16=int(h*18)
#    cv.rectangle(image,(W9,H5),(W10,H6),(0,0,255),2)


    for i in range(2):
        x0=int(w8*(i)+A8)
        x1=int(w8*(i+1)+A8)
        y0=H15
        y1=H16
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #2
#8配种评分
    #1
#    H1=int(h*5)
#    H2=int(h*9)
#    W11=int(w*73)
#    W12=int(w*90.5)
#    cv.rectangle(image,(W11,H1),(W12,H2),(0,0,255),2)
    
    H17=int(h*5.5)
    H18=int(h*8.5)
    w9=int(w*5.5)
    A8=int(w*73.5)
    for i in range(3):
        x0=int(w9*(i)+A8)
        x1=int(w9*(i+1)+A8)
        y0=H17
        y1=H18
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
    #2
    
#    H3=int(h*10)
#    H4=int(h*13)     
#    cv.rectangle(image,(W11,H4),(W12,H3),(0,0,255),2)
    H17=int(h*10)
    H18=int(h*13)
    for i in range(3):
        x0=int(w9*(i)+A8)
        x1=int(w9*(i+1)+A8)
        y0=H17
        y1=H18
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        print(x0,x1,y0,y1)
        print(ID)
#    #3
#    H5=int(h*15)
#    H6=int(h*18)
#    cv.rectangle(image,(W11,H5),(W12,H6),(0,0,255),2)
    H17=int(h*15)
    H18=int(h*18)
    for i in range(3):
        x0=int(w9*(i)+A8)
        x1=int(w9*(i+1)+A8)
        y0=H17
        y1=H18
        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
        ID=ID+1
        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
        info.append(info_array)
        print(x0,x1,y0,y1)
        print(ID)
    
    
    
#数据边框
##1.1
#    ID=0
##    cv.rectangle(image,(150,84),(730,168),(255,0,0),2)
#    X=[]
#    info=[]
#    QR=[]
#    w=int((73-15)/9)
##    print('1/***************************************')
#    for i in range(9):
#        x1=12+w*(i+1)
#        X.append(x1)
#
#    Y=10
#    for i in range(2):
#        y= Y+4*(i)
#        for j in range(len(X)):
#               y0=y-1
#               y1=y+1
#               x0=X[j]-2
#               x1=X[j]+2
##               cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#               ID=ID+1
##               info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
##               info.append(info_array)
##               print(info)
#               x0=x1=y0=y1=0
##2.1
##    cv.rectangle(image,(0,168),(365,438),(255,0,0),2)
##    cv.rectangle(image,(365,168),(730,438),(255,0,0),2)
#    X=[]
#    w=int((73-0)/4)
##    print('2/***************************************')
#    for i in range(2):
#        x1=0+w*(2*(i+1)-1)
#        X.append(x1)
#    y=30
##    print(len(X))
#    for j in range(len(X)):
#       y0=y-13
#       y1=y+13
#       x0=X[j]-17
#       x1=X[j]+17
##       y0=y-120
##       y1=y+120
##       x0=X[j]-165
##       x1=X[j]+165
#       if(j==0):
##           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#           cropped = image[y0:y1,x0:x1]
#           path='./1lw/'+photoName
#           cv.imwrite(path,cropped)
#           ID=ID+1
#           QR_array=decode_qr_code(ID,y0,y1,x0,x1,image)
#           QR.append(QR_array)
#           x0=x1=y0=y1=0
#       else:
##           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#           cropped = image[y0:y1,x0:x1]
#           path1='./2lw/'+photoName
#           cv.imwrite(path1,cropped)
#           ID=ID+1
#           QR_array=decode_qr_code(ID,y0,y1,x0,x1,image)
#           QR.append(QR_array)
#           x0=x1=y0=y1=0
#       
#
##2.3
##    cv.rectangle(image,(0,478),(730,675),(255,0,0),2)
#    X=[]
#    w=int((73-0)/12)
##    w=int((730-0)/24)
##    print('3/***************************************')
#    for i in range(12):
##        x1=8+w*(2*(i+1)-1)
##        x1=10+w*(2*(i+1)-1)
#        x1=w*(i+1)-2
#        X.append(x1)
#    Y=50
##    Y=498
#    for i in range(5):
#        y= Y+4*(i)
#        for j in range(len(X)):
#           y0=y-1
#           y1=y+1
#           x0=X[j]-2
#           x1=X[j]+2
##           y0=y-15
##           y1=y+15
##           x0=X[j]-25
##           x1=X[j]+25
##           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#           ID=ID+1
#           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#           info.append(info_array)
##           print(info)
##           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#           x0=x1=y0=y1=0
#
##2.4
##    cv.rectangle(image,(168,735),(750,900),(255,0,0),2)
#    X=[]
##    w=int((750-168)/10)
##    w=int((750-168)/20)
##    print('4/***************************************')
#    for i in range(10):
#        x1=14+w*(i+1)
##        x1=143+w*(2*(i+1)-1)
#        X.append(x1)
#    Y=76
##    Y=755
#    for i in range(4):
#        y= Y+4*(i)
#        for j in range(len(X)):
#           y0=y-1
#           y1=y+1
#           x0=X[j]-2
#           x1=X[j]+2
##           y0=y-15
##           y1=y+15
##           x0=X[j]-25
##           x1=X[j]+25
##           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#           ID=ID+1
#           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#           info.append(info_array)
##           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#           x0=x1=y0=y1=0
#
##2.5
##    cv.rectangle(image,(780,735),(1090,850),(255,0,0),2)
#    X=[]
#    w=int((109-78)/5)
##    print('5/15***************************************')
#    for i in range(5):
#        x1=75+w*(i+1)
##        x1=745+w*(i+1)
#        X.append(x1)
##    print(X)
##    第一行
##    Y=755
#    Y=76
#    for i in range(3):
#        y= Y+4*(i)
#        for j in range(len(X)):
#           y0=y-1
#           y1=y+1
#           x0=X[j]-2
#           x1=X[j]+2
##           y0=y-15
##           y1=y+15
##           x0=X[j]-25
##           x1=X[j]+25
##           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#           ID=ID+1
#           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#           info.append(info_array)
##           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#           x0=x1=y0=y1=0
#
##2.6
##    cv.rectangle(image,(910,632),(1195,675),(255,0,0),2)
#    X=[]
#    w=int((119-91)/2)
##    print('6/2***************************************')
#    for i in range(2):
#        x1=84+w*(i+1)
##        x1=837+w*(i+1)
#        X.append(x1)
#    y=65
#
#    for j in range(len(X)):
#       y0=y-1
#       y1=y+1
#       x0=X[j]-4
#       x1=X[j]+4
##       y0=y-15
##       y1=y+15
##       x0=X[j]-65
##       x1=X[j]+65
##       cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#       ID=ID+1
#       info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#       info.append(info_array)
##       info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#       x0=x1=y0=y1=0
#
#
##2.7
##    cv.rectangle(image,(970,210),(1195,600),(255,0,0),2)
#    X=[]
#    w=int((119-97)/3)
##    print('7/30***************************************')
#    for i in range(3):
#        x1=94+w*(i+1)
##        x1=935+w*(i+1)
#        X.append(x1)
#    Y=22
#
#    for i in range(1):
#        y= Y+4*(i)
#        for j  in range(len(X)):
#            y0=y-1
#            y1=y+1
#            x0=X[j]-2
#            x1=X[j]+2
##            y0=y-13
##            y1=y+13
##            x0=X[j]-34
##            x1=X[j]+34
##            cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#            ID=ID+1
#            info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#            info.append(info_array)
##            info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#            x0=x1=y0=y1=0
#
##2.8
##    cv.rectangle(image,(730,84),(840,168),(255,0,0),2)
#    X=[]
#    w=int((84-73)/2)
##    print('8/13***************************************')
#    for i in range(2):
#        x1=71+w*(i+1)
##        x1=705+w*(i+1)
#        X.append(x1)
#    Y=10
##    print(len(X))
#    for i in range(2):
#        y= Y+4*(i)
#        for j  in range(len(X)):
#            y0=y-1
#            y1=y+1
#            x0=X[j]-2
#            x1=X[j]+2
##            y0=y-13
##            y1=y+13
##            x0=X[j]-25
##            x1=X[j]+25
##            cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#            ID=ID+1
#            info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#            info.append(info_array)
##            info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#            x0=x1=y0=y1=0
##2.9
##    cv.rectangle(image,(870,42),(1080,168),(255,0,0),2)
#    X=[]
#    w=int((108-87)/3)
#    for i in range(3):
#        x1=84+w*(i+1)
##        x1=835+w*(i+1)
#        X.append(x1)
#    Y=6
##    print(len(X))
#    for i in range(3):
#        y= Y+4*(i)
#        for j  in range(len(X)):
#            y0=y-1
#            y1=y+1
#            x0=X[j]-2
#            x1=X[j]+2            
##            y0=y-13
##            y1=y+13
##            x0=X[j]-25
##            x1=X[j]+25
##            cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#            ID=ID+1
#            info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#            info.append(info_array)
##            info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
#            x0=x1=y0=y1=0
#
##    cv.imwrite(savefilepname,image)
#    return image,info,QR
    
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
#        print('照片总张数',len(name))