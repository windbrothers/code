# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:16:53 2020

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
from product_QRCode import decode_qr_code
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

def shengchengshuju(ID,y0,y1,x0,x1,image):
    name='./1cut/'
    X=random.randint(1,10000000)
    num=1
    savename=name+str(X)+str(ID)+str(num)+'.jpg'
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

def bianji(image,photoName):
    ID=0
#    cv.rectangle(image,(150,84),(730,168),(255,0,0),2)
    X=[]
    info=[]
    QR=[]
    w=int((730-150)/9)
#    print('1/***************************************')
    for i in range(9):
        x1=120+w*(i+1)
        X.append(x1)

    Y=105
    for i in range(2):
        y= Y+40*(i)
        for j in range(len(X)):
               y0=y-15
               y1=y+15
               x0=X[j]-25
               x1=X[j]+25
#               cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
               ID=ID+1
               info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
               info.append(info_array)
#               print(info)
               x0=x1=y0=y1=0
    X=[]
    w=int((730-0)/4)
#    print('2/***************************************')
    for i in range(2):
        x1=0+w*(2*(i+1)-1)
        X.append(x1)
    y=303
#    print(len(X))
    for j in range(len(X)):
       y0=y-130
       y1=y+130
       x0=X[j]-175
       x1=X[j]+175
#       y0=y-120
#       y1=y+120
#       x0=X[j]-165
#       x1=X[j]+165
       if(j==0):
#           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
           cropped = image[y0:y1,x0:x1]
           path='./1lw/'+photoName
           cv.imwrite(path,cropped)
           ID=ID+1
           QR_array=decode_qr_code(ID,y0,y1,x0,x1,image)
           QR.append(QR_array)
           x0=x1=y0=y1=0
       else:
#           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
           cropped = image[y0:y1,x0:x1]
           path1='./2lw/'+photoName
           cv.imwrite(path1,cropped)
           ID=ID+1
           QR_array=decode_qr_code(ID,y0,y1,x0,x1,image)
           QR.append(QR_array)
           x0=x1=y0=y1=0
       

#2.3
#    cv.rectangle(image,(0,478),(730,675),(255,0,0),2)
    X=[]
    w=int((730-0)/12)
#    w=int((730-0)/24)
#    print('3/***************************************')
    for i in range(12):
#        x1=8+w*(2*(i+1)-1)
#        x1=10+w*(2*(i+1)-1)
        x1=w*(i+1)-18
        X.append(x1)
    Y=506
#    Y=498
    for i in range(5):
        y= Y+40*(i)
        for j in range(len(X)):
           y0=y-13
           y1=y+13
           x0=X[j]-15
           x1=X[j]+15
#           y0=y-15
#           y1=y+15
#           x0=X[j]-25
#           x1=X[j]+25
#           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
           ID=ID+1
           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
           info.append(info_array)
#           print(info)
#           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
           x0=x1=y0=y1=0

#2.4
#    cv.rectangle(image,(168,735),(750,900),(255,0,0),2)
    X=[]
#    w=int((750-168)/10)
#    w=int((750-168)/20)
#    print('4/***************************************')
    for i in range(10):
        x1=143+w*(i+1)
#        x1=143+w*(2*(i+1)-1)
        X.append(x1)
    Y=763
#    Y=755
    for i in range(4):
        y= Y+40*(i)
        for j in range(len(X)):
           y0=y-13
           y1=y+13
           x0=X[j]-15
           x1=X[j]+15
#           y0=y-15
#           y1=y+15
#           x0=X[j]-25
#           x1=X[j]+25
#           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
           ID=ID+1
           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
           info.append(info_array)
#           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
           x0=x1=y0=y1=0

#2.5
#    cv.rectangle(image,(780,735),(1090,850),(255,0,0),2)
    X=[]
    w=int((1090-780)/5)
#    print('5/15***************************************')
    for i in range(5):
        x1=750+w*(i+1)
#        x1=745+w*(i+1)
        X.append(x1)
#    print(X)
#    第一行
#    Y=755
    Y=763
    for i in range(3):
        y= Y+40*(i)
        for j in range(len(X)):
           y0=y-13
           y1=y+13
           x0=X[j]-15
           x1=X[j]+15
#           y0=y-15
#           y1=y+15
#           x0=X[j]-25
#           x1=X[j]+25
#           cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
           ID=ID+1
           info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
           info.append(info_array)
#           info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
           x0=x1=y0=y1=0

#2.6
#    cv.rectangle(image,(910,632),(1195,675),(255,0,0),2)
    X=[]
    w=int((1195-910)/2)
#    print('6/2***************************************')
    for i in range(2):
        x1=843+w*(i+1)
#        x1=837+w*(i+1)
        X.append(x1)
    y=654

    for j in range(len(X)):
       y0=y-13
       y1=y+13
       x0=X[j]-40
       x1=X[j]+40
#       y0=y-15
#       y1=y+15
#       x0=X[j]-65
#       x1=X[j]+65
#       cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
       ID=ID+1
       info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
       info.append(info_array)
#       info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
       x0=x1=y0=y1=0


#2.7
#    cv.rectangle(image,(970,210),(1195,600),(255,0,0),2)
    X=[]
    w=int((1195-970)/3)
#    print('7/30***************************************')
    for i in range(3):
        x1=940+w*(i+1)
#        x1=935+w*(i+1)
        X.append(x1)
    Y=225

    for i in range(10):
        y= Y+40*(i)
        for j  in range(len(X)):
            y0=y-8
            y1=y+8
            x0=X[j]-20
            x1=X[j]+20
#            y0=y-13
#            y1=y+13
#            x0=X[j]-34
#            x1=X[j]+34
#            cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
            ID=ID+1
            info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
            info.append(info_array)
#            info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
            x0=x1=y0=y1=0

#2.8
#    cv.rectangle(image,(730,84),(840,168),(255,0,0),2)
    X=[]
    w=int((840-730)/2)
#    print('8/13***************************************')
    for i in range(2):
        x1=710+w*(i+1)
#        x1=705+w*(i+1)
        X.append(x1)
    Y=105
#    print(len(X))
    for i in range(2):
        y= Y+40*(i)
        for j  in range(len(X)):
            y0=y-13
            y1=y+13
            x0=X[j]-15
            x1=X[j]+15
#            y0=y-13
#            y1=y+13
#            x0=X[j]-25
#            x1=X[j]+25
#            cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
            ID=ID+1
            info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
            info.append(info_array)
#            info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
            x0=x1=y0=y1=0
#2.9
#    cv.rectangle(image,(870,42),(1080,168),(255,0,0),2)
    X=[]
    w=int((1080-870)/3)
    for i in range(3):
        x1=840+w*(i+1)
#        x1=835+w*(i+1)
        X.append(x1)
    Y=65
#    print(len(X))
    for i in range(3):
        y= Y+40*(i)
        for j  in range(len(X)):
            y0=y-13
            y1=y+13
            x0=X[j]-15
            x1=X[j]+15            
#            y0=y-13
#            y1=y+13
#            x0=X[j]-25
#            x1=X[j]+25
#            cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
            ID=ID+1
            info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
            info.append(info_array)
#            info=shengchengshuju(ID,y0,y1,x0,x1,image,info)
            x0=x1=y0=y1=0

#    cv.imwrite(savefilepname,image)
#    return image,info,QR
if __name__ == '__main__':
        Sum =0
        filepath='./cut/'
        for filename in os.listdir(filepath):
            path = filepath+filename
            x,mask=decode_qr_code(path,filename)
            bianji(mask,filename)
            Sum=Sum+x
        print('识别成功的二维码张数',Sum)