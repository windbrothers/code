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
def shengchengshuju(ID,y0,y1,x0,x1,image,photoName):
    name='./cut3/'
    e=y0
    r=y1
    q=x0
    w=x1
#    X=random.randint(1,10000000)
    savename=name+str(photoName)+'1_'+str(ID)+'.jpg'
    K=3
    X_L=int((abs(x0-x1)/2)/K)
    X_L1=int((abs(x0-x1)/3)/K)
    center_point_x=int(abs(x0+x1)/2)
    x0=int(center_point_x-X_L)
    x1=int(x1-X_L1)
    cropped = image[y0:y1,x0:x1]
    cropped=cv.resize(cropped,(400,300))
    cv.imwrite(savename,cropped)
#3333333333
    # remove blue color
    hsv = cv.cvtColor(cropped, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([156, 43, 46])
    upper_hsv = np.array([180, 255, 255])
    mask = cv.inRange(hsv, lowerb = lower_hsv, upperb = upper_hsv)
    lower_hsv2 = np.array([0, 43, 46])
    upper_hsv2 = np.array([10, 255, 255])
    mask2 = cv.inRange(hsv, lowerb = lower_hsv2, upperb = upper_hsv2)
    Mask = mask+mask2
#    pint_W=Mask.shape[0]-1
#    pint_H=Mask.shape[1]-1
#    area=(pint_W+1)*(pint_H+1)
#    Wk=0#Wk 白色
#    Bk=0#Bk 黑色
    
#    for i in range(pint_W):
#        for j in range(pint_H):
#            if(Mask[i][j]==255):
#                Wk=Wk+1
##                print(Wk)
#            elif(Mask[i][j]==0):
#                Bk=Bk+1
##                print(Bk)
#            else:
#                print('error!')
#    R=Wk/area
    average = Mask.mean(axis=0).mean(axis=0)
#    print(ID,average,photoName)
    ptStart = (q, e)
    ptEnd = (w, r)
    ptStart1 = (q, r)
    ptEnd1 = (w, e)
    if(average>90):
#    if(R>0.3):
        cv.line(image, ptStart, ptEnd, (255, 0, 0), 1, 4)
        cv.line(image, ptStart1, ptEnd1, (255, 0, 0), 1, 4)
        sign=1
        return ID
    else:
        sign=0
        return 0
    print(ID,sign)
#    return ID,sign



def resize_Photo(path,filename):
    Mask=cv.imread(path)
    print(Mask.shape)
    h=int(Mask.shape[0]/3)
    w=int(Mask.shape[1]/3)
    print(w,h)
#    Mask=cv.resize(Mask,(400,300))
    Mask=cv.resize(Mask,(1200,900))
#    Mask=cv.resize(Mask,(1200,900))

    return 1,Mask
def bianji(image,photoName):
#    image = image.resize((400, 300))

    H=image.shape[0]
    W=image.shape[1]

#    print('高度',H)
#    print('宽度',W)
#外边框
#A的宽度=75
    W_A=75
    W_b_A_1=0
    W_b_A_2=W_A
    W_e_A_1=W-W_A
    W_e_A_2=W
    
    W1=70*0+W_A
    W2=70*1+W_A
    W3=70*2+W_A
    W4=70*3+W_A
    W5=70*4+W_A
    W6=70*5+W_A
    W7=70*6+W_A
    W8=70*7+W_A
    W9=70*8+W_A
    W10=70*9+W_A
    W11=70*10+W_A
    W12=70*11+W_A
    W13=70*12+W_A
    W14=70*13+W_A
    W15=70*14+W_A
    W16=70*15+W_A
#边界
    cv.rectangle(image,(W_b_A_1,0),(W_b_A_2,900),(0,255,255),2)
    cv.rectangle(image,(W_e_A_1,0),(W_e_A_2,900),(0,255,255),2)
    cv.rectangle(image,(W_b_A_1,0),(W_e_A_2,900),(0,255,255),2)
#1品种
    H1_0=0
    H1_1=42
    cv.rectangle(image,(W_b_A_2,H1_0),(W_e_A_1,H1_1),(0,255,255),2)
#    1.1切割
    cv.rectangle(image,(W1,H1_0),(W2,H1_1),(255,0,255),2)
    cv.rectangle(image,(W2,H1_0),(W4,H1_1),(255,0,255),2)
    cv.rectangle(image,(W4,H1_0),(W6,H1_1),(255,0,255),2)
    cv.rectangle(image,(W6,H1_0),(W8,H1_1),(255,0,255),2)
    cv.rectangle(image,(W8,H1_0),(W10,H1_1),(255,0,255),2)
    cv.rectangle(image,(W10,H1_0),(W12,H1_1),(255,0,255),2)
    cv.rectangle(image,(W12,H1_0),(W14,H1_1),(255,0,255),2)
    cv.rectangle(image,(W14,H1_0),(W16,H1_1),(255,0,255),2)
#2书写数据日期
    H2_0=42
    H2_1=42+39
    cv.rectangle(image,(W_b_A_2,H2_0),(W_e_A_1,H2_1),(0,255,255),2)
#    2.1切割
    
    cv.rectangle(image,(W1,H2_0),(W2,H2_1),(255,0,255),2)
    cv.rectangle(image,(W2,H2_0),(W3,H2_1),(255,0,255),2)
    cv.rectangle(image,(W3,H2_0),(W4,H2_1),(255,0,255),2)
    cv.rectangle(image,(W4,H2_0),(W5,H2_1),(255,0,255),2)
    cv.rectangle(image,(W5,H2_0),(W6,H2_1),(255,0,255),2)
    cv.rectangle(image,(W6,H2_0),(W7,H2_1),(255,0,255),2)
    cv.rectangle(image,(W7,H2_0),(W8,H2_1),(255,0,255),2)
    cv.rectangle(image,(W8,H2_0),(W9,H2_1),(255,0,255),2)
    cv.rectangle(image,(W9,H2_0),(W10,H2_1),(255,0,255),2)
    cv.rectangle(image,(W10,H2_0),(W11,H2_1),(255,0,255),2)
    cv.rectangle(image,(W11,H2_0),(W12,H2_1),(255,0,255),2)
    cv.rectangle(image,(W12,H2_0),(W13,H2_1),(255,0,255),2)
    cv.rectangle(image,(W13,H2_0),(W14,H2_1),(255,0,255),2)
    cv.rectangle(image,(W14,H2_0),(W15,H2_1),(255,0,255),2)
    cv.rectangle(image,(W15,H2_0),(W16,H2_1),(255,0,255),2)
    
    H2_0=42
    H2_1=42+39*2
#    2.1切割
    cv.rectangle(image,(W_b_A_2,H2_0),(W_e_A_1,H2_1),(0,255,255),2)
    cv.rectangle(image,(W1,H2_0),(W2,H2_1),(255,0,255),2)
    cv.rectangle(image,(W2,H2_0),(W3,H2_1),(255,0,255),2)
    cv.rectangle(image,(W3,H2_0),(W4,H2_1),(255,0,255),2)
    cv.rectangle(image,(W4,H2_0),(W5,H2_1),(255,0,255),2)
    cv.rectangle(image,(W5,H2_0),(W6,H2_1),(255,0,255),2)
    cv.rectangle(image,(W6,H2_0),(W7,H2_1),(255,0,255),2)
    cv.rectangle(image,(W7,H2_0),(W8,H2_1),(255,0,255),2)
    cv.rectangle(image,(W8,H2_0),(W9,H2_1),(255,0,255),2)
    cv.rectangle(image,(W9,H2_0),(W10,H2_1),(255,0,255),2)
    cv.rectangle(image,(W10,H2_0),(W11,H2_1),(255,0,255),2)
    cv.rectangle(image,(W11,H2_0),(W12,H2_1),(255,0,255),2)
    cv.rectangle(image,(W12,H2_0),(W13,H2_1),(255,0,255),2)
    cv.rectangle(image,(W13,H2_0),(W14,H2_1),(255,0,255),2)
    cv.rectangle(image,(W14,H2_0),(W15,H2_1),(255,0,255),2)
    cv.rectangle(image,(W15,H2_0),(W16,H2_1),(255,0,255),2)
    
    
#333#!识别区
    ID=1
    QR_info=[]
#    cv.rectangle(image,(150,84),(730,168),(255,0,0),2)
    X=[]
    info=[]

    
#3发情次数 1-12
    H3_0=42+39*2
    H3_1=42+39*2+45
#    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W1,H3_0),(W2,H3_1),(155,155,255),2)
    cv.rectangle(image,(W2,H3_0),(W3,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H3_0),(W4,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H3_0),(W5,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H3_0),(W6,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H3_0),(W7,H3_1),(155,155,255),2)    
    cv.rectangle(image,(W7,H3_0),(W8,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H3_0),(W9,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H3_0),(W10,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H3_0),(W11,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H3_0),(W12,H3_1),(155,155,255),2)    
    cv.rectangle(image,(W12,H3_0),(W13,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H3_0),(W14,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1    
    cv.rectangle(image,(W14,H3_0),(W15,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1    
    cv.rectangle(image,(W15,H3_0),(W16,H3_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H3_0,H3_1,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1

###4二维码/背标
    H4_0=42+39*2+45
    H4_1=42+39*3+45*5
    cv.rectangle(image,(W_b_A_2,H4_0),(W_e_A_1,H4_1),(0,255,255),2)
#    4.1二维码
    cv.rectangle(image,(W1,H4_0),(W5,H4_1),(155,255,0),2)
    QR_ID=181
    info_array=shengchengshuju(QR_ID,H4_0,H4_1,W1,W5,image,photoName)
    info.append(info_array)
#    QR_array=decode_qr_code(QR_ID,y0,y1,x0,x1,image)
#    QR_info.append(QR_array)
    cv.rectangle(image,(W5,H4_0),(W9,H4_1),(155,255,0),2)
    QR_ID=182
    info_array=shengchengshuju(QR_ID,H4_0,H4_1,W5,W9,image,photoName)
    info.append(info_array)
#    QR_array=decode_qr_code(QR_ID,y0,y1,x0,x1,image)
#    QR_info.append(QR_array)
    
#    4.2标题
    H4_0=42+39*2+45
    H4_1=42+39*3+45
    cv.rectangle(image,(W9,H4_0),(W12,H4_1),(155,155,255),2)
    cv.rectangle(image,(W12,H4_0),(W14,H4_1),(155,155,255),2)
    cv.rectangle(image,(W14,H4_0),(W16,H4_1),(155,155,255),2)
#    4.2取值
    H4_0=42+39*3+45
    H4_1=42+39*3+45*2
    cv.rectangle(image,(W9,H4_0),(W10,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W10,H4_0),(W11,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W11,H4_0),(W12,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H4_0),(W13,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H4_0),(W14,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H4_0),(W15,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H4_0),(W16,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1

    H4_0=42+39*3+45*2
    H4_1=42+39*3+45*3
    cv.rectangle(image,(W9,H4_0),(W10,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W10,H4_0),(W11,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W11,H4_0),(W12,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H4_0),(W13,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H4_0),(W14,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H4_0),(W15,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H4_0),(W16,H4_1),(155,255,0),2)

    H4_0=42+39*3+45*3
    H4_1=42+39*3+45*4
    cv.rectangle(image,(W9,H4_0),(W10,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W10,H4_0),(W11,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W11,H4_0),(W12,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H4_0),(W13,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H4_0),(W14,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H4_0),(W15,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H4_0),(W16,H4_1),(155,255,0),2)
    H4_0=42+39*3+45*4
    H4_1=42+39*3+45*5
    cv.rectangle(image,(W9,H4_0),(W10,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W10,H4_0),(W11,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1  
    cv.rectangle(image,(W11,H4_0),(W12,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H4_0),(W13,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H4_0),(W14,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H4_0),(W15,H4_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H4_0,H4_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H4_0),(W16,H4_1),(155,255,0),2)
    
###5胎次
    H5_0=42+39*3+45*5
    H5_1=42+39*4+45*10
    cv.rectangle(image,(W_b_A_2,H5_0),(W_e_A_1,H5_1),(0,255,255),2)
#    5.1标题
    H5_0=42+39*3+45*5
    H5_1=42+39*4+45*5
    cv.rectangle(image,(W1,H5_0),(W2,H5_1),(155,155,255),2)
    cv.rectangle(image,(W2,H5_0),(W3,H5_1),(155,155,255),2)
    cv.rectangle(image,(W3,H5_0),(W4,H5_1),(155,155,255),2)
    cv.rectangle(image,(W4,H5_0),(W5,H5_1),(155,155,255),2)
    cv.rectangle(image,(W5,H5_0),(W6,H5_1),(155,155,255),2)
    cv.rectangle(image,(W6,H5_0),(W7,H5_1),(155,155,255),2)
    cv.rectangle(image,(W7,H5_0),(W8,H5_1),(155,155,255),2)
    cv.rectangle(image,(W8,H5_0),(W10,H5_1),(155,155,255),2)
    cv.rectangle(image,(W10,H5_0),(W12,H5_1),(155,155,255),2)
    cv.rectangle(image,(W12,H5_0),(W13,H5_1),(155,155,255),2)
    cv.rectangle(image,(W13,H5_0),(W16,H5_1),(155,155,255),2)
#    5.2切割
    H5_0=42+39*4+45*5
    H5_1=42+39*4+45*6
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W1,H5_0),(W2,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H5_0),(W3,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H5_0),(W4,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H5_0),(W5,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H5_0),(W6,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H5_0),(W7,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H5_0),(W8,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H5_0),(W9,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H5_0),(W10,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H5_0),(W11,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H5_0),(W12,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H5_0),(W13,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H5_0),(W14,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H5_0),(W15,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H5_0),(W16,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    H5_0=42+39*4+45*6
    H5_1=42+39*4+45*7
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W1,H5_0),(W2,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H5_0),(W3,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H5_0),(W4,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H5_0),(W5,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H5_0),(W6,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H5_0),(W7,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H5_0),(W8,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H5_0),(W9,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H5_0),(W10,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H5_0),(W11,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H5_0),(W12,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H5_0),(W13,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H5_0),(W14,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H5_0),(W15,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H5_0),(W16,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    H5_0=42+39*4+45*7
    H5_1=42+39*4+45*8
    cv.rectangle(image,(W1,H5_0),(W2,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H5_0),(W3,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H5_0),(W4,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H5_0),(W5,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H5_0),(W6,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H5_0),(W7,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H5_0),(W8,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H5_0),(W9,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H5_0),(W10,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H5_0),(W11,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H5_0),(W12,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H5_0),(W13,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H5_0),(W14,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H5_0),(W15,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H5_0),(W16,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    H5_0=42+39*4+45*8
    H5_1=42+39*4+45*9
    cv.rectangle(image,(W1,H5_0),(W2,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H5_0),(W3,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H5_0),(W4,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H5_0),(W5,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H5_0),(W6,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H5_0),(W7,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H5_0),(W8,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H5_0),(W9,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H5_0),(W10,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H5_0),(W11,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H5_0),(W12,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H5_0),(W13,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H5_0),(W14,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H5_0),(W15,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H5_0),(W16,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    H5_0=42+39*4+45*9
    H5_1=42+39*4+45*10
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W1,H5_0),(W2,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H5_0),(W3,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H5_0),(W4,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H5_0),(W5,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H5_0),(W6,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H5_0),(W7,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H5_0),(W8,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H5_0),(W9,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H5_0),(W10,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H5_0),(W12,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W10,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H5_0),(W13,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H5_0),(W14,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H5_0),(W16,H5_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H5_0,H5_1,W14,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
###6免疫
    
    H6_01=42+39*4+45*10
    H6_11=42+39*5+45*13
    cv.rectangle(image,(W_b_A_2,H6_01),(W_e_A_1,H6_11),(0,255,255),2)
#    6.1标题
    H6_0=42+39*4+45*10
    H6_1=42+39*5+45*10
    H6_6=42+39*5+45*12
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
#    cv.rectangle(image,(W1,H6_0),(W2,H6_1),(155,155,255),2)
    cv.rectangle(image,(W2,H6_0),(W3,H6_1),(155,155,255),2)
    cv.rectangle(image,(W3,H6_0),(W4,H6_1),(155,155,255),2)
    cv.rectangle(image,(W4,H6_0),(W5,H6_1),(155,155,255),2)
    cv.rectangle(image,(W5,H6_0),(W6,H6_1),(155,155,255),2)
    cv.rectangle(image,(W6,H6_0),(W7,H6_1),(155,155,255),2)
    cv.rectangle(image,(W7,H6_0),(W8,H6_1),(155,155,255),2)
    cv.rectangle(image,(W8,H6_0),(W9,H6_1),(155,155,255),2)
    cv.rectangle(image,(W9,H6_0),(W10,H6_1),(155,155,255),2)
    cv.rectangle(image,(W10,H6_0),(W11,H6_1),(155,155,255),2)
    cv.rectangle(image,(W11,H6_0),(W12,H6_1),(155,155,255),2)
    cv.rectangle(image,(W12,H6_0),(W13,H6_1),(155,155,255),2)
    cv.rectangle(image,(W13,H6_0),(W14,H6_1),(155,155,255),2)
    cv.rectangle(image,(W14,H6_0),(W15,H6_1),(155,155,255),2)
    cv.rectangle(image,(W15,H6_0),(W16,H6_1),(155,155,255),2)
#    左
    cv.rectangle(image,(W1,H6_01),(W2,H6_11),(155,155,255),2)
    
    cv.rectangle(image,(W2,H6_01),(W3,H6_6),(155,155,255),2)
    cv.rectangle(image,(W2,H6_11),(W3,H6_6),(155,155,255),2)
#    6.2数据
    H6_0=42+39*5+45*10
    H6_1=42+39*5+45*11
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W3,H6_0),(W4,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H6_0),(W5,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H6_0),(W6,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H6_0),(W7,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H6_0),(W8,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H6_0),(W9,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H6_0),(W10,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H6_0),(W11,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H6_0),(W12,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H6_0),(W13,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H6_0),(W14,H6_1),(155,155,255),2)
    cv.rectangle(image,(W14,H6_0),(W15,H6_1),(155,155,255),2)
    cv.rectangle(image,(W15,H6_0),(W16,H6_1),(155,155,255),2)
    H6_0=42+39*5+45*11
    H6_1=42+39*5+45*12
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W3,H6_0),(W4,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H6_0),(W5,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H6_0),(W6,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H6_0),(W7,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H6_0),(W8,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H6_0),(W9,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H6_0),(W10,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H6_0),(W11,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H6_0),(W12,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H6_0),(W13,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H6_0),(W14,H6_1),(155,155,255),2)
    cv.rectangle(image,(W14,H6_0),(W15,H6_1),(155,155,255),2)
    cv.rectangle(image,(W15,H6_0),(W16,H6_1),(155,155,255),2)
    H6_0=42+39*5+45*12
    H6_1=42+39*5+45*13
    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W3,H6_0),(W4,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H6_0),(W5,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H6_0),(W6,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H6_0),(W7,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H6_0),(W8,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H6_0),(W9,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H6_0),(W10,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H6_0),(W11,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H6_0),(W12,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H6_0),(W13,H6_1),(155,255,0),2)
    info_array=shengchengshuju(ID,H6_0,H6_1,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H6_0),(W14,H6_1),(155,155,255),2)
    cv.rectangle(image,(W14,H6_0),(W15,H6_1),(155,155,255),2)
    cv.rectangle(image,(W15,H6_0),(W16,H6_1),(155,155,255),2)
    
    print('ID,x0,x1;y0,y1',int(ID-1),W2,W3,H3_0,H3_1)
#7书写数据日期
    H7_0=42+39*5+45*13
    H7_1=42+39*6+45*13
    cv.rectangle(image,(W_b_A_2,H7_0),(W_e_A_1,H7_1),(0,255,255),2)
    cv.rectangle(image,(W1,H7_0),(W4,H7_1),(255,0,255),2)
    cv.rectangle(image,(W4,H7_0),(W9,H7_1),(255,0,255),2)
    cv.rectangle(image,(W9,H7_0),(W12,H7_1),(255,0,255),2)
    cv.rectangle(image,(W12,H7_0),(W16,H7_1),(255,0,255),2)
    H7_0=42+39*6+45*13
    H7_1=42+39*7+45*13
    cv.rectangle(image,(W_b_A_2,H7_0),(W_e_A_1,H7_1),(0,255,255),2)
    cv.rectangle(image,(W1,H7_0),(W16,H7_1),(255,0,255),2)
#    HH=int(h*50)    #24
##    cv.rectangle(image,(0,H6),(W2,HH),(0,0,255),2)
#    w2=int(31*w)
#    A3=int(0)
#    for i in range(2):
#        x0=int(w2*(i)+A3)
#        x1=int(w2*(i+1)+A3)
#        y0=H6
#        y1=HH
##        cv.rectangle(image,(x0,y0),(x1,y1),(255,255,0),2)
#        ID=ID+1
#        info_array=shengchengshuju(ID,y0,y1,x0,x1,image)
#        info.append(info_array)
##        print(x0,x1,y0,y1)
#        print(ID)
    
    image=cv.resize(image,(1200,900))
    cv.imwrite('./ReSize/'+filename,image)
#    print(info)
    return info
# card_key=[
#'X','begin-ordinal_1','end-ordinal_1','X','begin-ordinal_2','end-ordinal_2','X','begin-ordinal_3','end-ordinal_3','X','begin-ordinal_4','end-ordinal_4','X','begin-ordinal_5','end-ordinal_5',
#'X','begin-ordinal_6','end-ordinal_6','birth_number-1','quantity2-10','quantity3-10','quantity6-10','quantity4-10','quantity5-10','quantity7-10','birth_weight-10','birth_weight-4','wean_quantity-10',
#'total_weight-10','total_weight-1','birth_number-2','quantity2-1','quantity3-1','quantity6-1','quantity4-1','quantity5-1','quantity7-1','birth_weight-20','birth_weight-5','wean_quantity-1','total_weight-20',
#'total_weight-2','birth_number-3','quantity2-2','quantity3-2','quantity6-2','quantity4-2','quantity5-2','quantity7-2','birth_weight-30','birth_weight-6','wean_quantity-2','total_weight-30','total_weight-3',
#'birth_number-4','quantity2-3','quantity3-3','quantity6-3','quantity4-3','quantity5-3','quantity7-3','birth_weight-1','birth_weight-7','wean_quantity-3','total_weight-40','total_weight-4','birth_number-5',
#'quantity2-4','quantity3-4','quantity6-4','quantity4-4','quantity5-4','quantity7-4','birth_weight-2','birth_weight-8','wean_quantity-4','total_weight-50','total_weight-5','vaccines1-muzhu_1','vaccines2-muzhu_1',
#'vaccines3-muzhu_1','vaccines4-muzhu_1','vaccines5-muzhu_1','vaccines6-muzhu_1','vaccines7-muzhu_1','vaccines8-muzhu_1','vaccines9-muzhu_1','vaccines10-muzhu_1','vaccines1-muzhu_2','vaccines2-muzhu_2',
#'vaccines3-muzhu_2','vaccines4-muzhu_2','vaccines5-muzhu_2','vaccines6-muzhu_2','vaccines7-muzhu_2','vaccines8-muzhu_2','vaccines9-muzhu_2','vaccines10-muzhu_2','vaccines1-muzhu_3','vaccines2-muzhu_3',
#'vaccines3-muzhu_3','vaccines4-muzhu_3','vaccines5-muzhu_3','vaccines6-muzhu_3','vaccines7-muzhu_3','vaccines8-muzhu_3','vaccines9-muzhu_3','vaccines10-muzhu_3','vaccines1-zizhu_1','vaccines2-zizhu_1',
#'vaccines3-zizhu_1','vaccines4-zizhu_1','vaccines5-zizhu_1','vaccines6-zizhu_1','vaccines7-zizhu_1','vaccines8-zizhu_1','vaccines9-zizhu_1','vaccines10-zizhu_1','thickness-before_mating','hickness-gestation_30_day',
#'thickness-gestation_75_days','thickness-gestation_90_days','thickness-before_obstetric','thickness-20','thickness-10','thickness-9','thickness-8','thickness-7','thickness-6','thickness-5','thickness-4',
#'thickness-3','thickness-2','SC-birth_code','ZC-birth_code','Y4-ordinal_1','Y3-ordinal_1','Y5-ordinal_1','Y4-ordinal_2','Y3-ordinal_2','Y5-ordinal_2','Y4-ordinal_3','Y3-ordinal_3','Y5-ordinal_3','Y4-ordinal_4',
#'Y3-ordinal_4','Y5-ordinal_4','Y4-ordinal_5','Y3-ordinal_5','Y5-ordinal_5','Y4-ordinal_6','Y3-ordinal_6','Y5-ordinal_6','Y4-ordinal_7','Y3-ordinal_7','Y5-ordinal_7','Y4-ordinal_8','Y3-ordinal_8','Y5-ordinal_8',
#'Y4-ordinal_9','Y3-ordinal_9','Y5-ordinal_9','Y4-ordinal_10','Y3-ordinal_10','Y5-ordinal_10','operation_name-A','operation_name-B','operation_name-C','operation_name-D','score_1-breeding_1','score_1-breeding_2',
#'score_1-breeding_3','score_2-breeding_1','score_2-breeding_2','score_2-breeding_3','score_3-breeding_1','score_3-breeding_2','score_3-breeding_3'
#]
    
if __name__ == '__main__':
        Sum =0
        filepath='./cut/'
        for filename in os.listdir(filepath):
            path = filepath+filename
            x,mask=resize_Photo(path,filename)
            Info=bianji(mask,filename)
            b = [str for str in Info if str not in [0]]
            print(b)
            Sum=Sum+x
        print('识别成功的二维码张数',Sum)
        
#                Orig_url = filepath+filename
#                url.append(Orig_url)
#        #        print(Orig_url)
#                photoName=Orig_url.split("/")[-1]
##                name.append(photoName)
#        print('照片总张数',len(name))# 