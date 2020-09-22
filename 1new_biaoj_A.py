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
#    K=3
#    X_L=int((abs(x0-x1)/2)/K)
#    X_L1=int((abs(x0-x1)/3)/K)
#    center_point_x=int(abs(x0+x1)/2)
#    x0=int(center_point_x-X_L)
#    x1=int(x1-X_L1)
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
    print(ID,average,photoName)
    ptStart = (q, e)
    ptEnd = (w, r)
    ptStart1 = (q, r)
    ptEnd1 = (w, e)
    if(average>10):
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
    K=44
    KK=40
    H1=0
    H2=K
    H3=K*2
    H4=K*3
    H5=K*3+KK
    H6=K*3+KK*2
    H7=K*3+KK*3
    H8=K*3+KK*4
    H9=K*3+KK*5
    H10=K*3+KK*6
    H11=K*3+KK*7
    H12=K*3+KK*8
    H13=K*3+KK*9
    H14=K*3+KK*10
    H15=K*3+KK*11
    H16=K*3+KK*12
    H17=K*3+KK*13
    H18=K*3+KK*14
    H19=K*3+KK*15
    H20=K*3+KK*16
    H21=K*3+KK*17
    H22=K*4+KK*17
    H23=K*5+KK*17

#边界
    cv.rectangle(image,(W_b_A_1,0),(W_b_A_2,900),(0,255,255),2)
    cv.rectangle(image,(W_e_A_1,0),(W_e_A_2,900),(0,255,255),2)
    cv.rectangle(image,(W_b_A_1,0),(W_e_A_2,900),(0,255,255),2)
#1品种
#    1.1切割
    cv.rectangle(image,(W1,H1),(W2,H2),(255,0,255),2)
    cv.rectangle(image,(W2,H1),(W4,H2),(255,0,255),2)
    cv.rectangle(image,(W4,H1),(W6,H2),(255,0,255),2)
    cv.rectangle(image,(W6,H1),(W8,H2),(255,0,255),2)
    cv.rectangle(image,(W8,H1),(W10,H2),(255,0,255),2)
    cv.rectangle(image,(W10,H1),(W12,H2),(255,0,255),2)
    cv.rectangle(image,(W12,H1),(W14,H2),(255,0,255),2)
    cv.rectangle(image,(W14,H1),(W16,H2),(255,0,255),2)
#2书写数据日期
    H2_0=44
    H2_1=44*2
    cv.rectangle(image,(W_b_A_2,H2_0),(W_e_A_1,H2_1),(0,255,255),2)
#    2.1切割 开始日期
    cv.rectangle(image,(W1,H2),(W2,H3),(255,0,255),2)
    cv.rectangle(image,(W2,H2),(W3,H3),(255,0,255),2)
    cv.rectangle(image,(W3,H2),(W4,H3),(255,0,255),2)
    cv.rectangle(image,(W4,H2),(W5,H3),(255,0,255),2)
    cv.rectangle(image,(W5,H2),(W6,H3),(255,0,255),2)
    cv.rectangle(image,(W6,H2),(W7,H3),(255,0,255),2)
    cv.rectangle(image,(W7,H2),(W8,H3),(255,0,255),2)
    cv.rectangle(image,(W8,H2),(W9,H3),(255,0,255),2)
    cv.rectangle(image,(W9,H2),(W10,H3),(255,0,255),2)
    cv.rectangle(image,(W10,H2),(W11,H3),(255,0,255),2)
    cv.rectangle(image,(W11,H2),(W12,H3),(255,0,255),2)
    cv.rectangle(image,(W12,H2),(W13,H3),(255,0,255),2)
    cv.rectangle(image,(W13,H2),(W14,H3),(255,0,255),2)
    cv.rectangle(image,(W14,H2),(W15,H3),(255,0,255),2)
    cv.rectangle(image,(W15,H2),(W16,H3),(255,0,255),2)
    
    H2_0=44*2
    H2_1=44*3
#    2.2切割 结束日期
    cv.rectangle(image,(W_b_A_2,H2_0),(W_e_A_1,H2_1),(0,255,255),2)
    cv.rectangle(image,(W1,H3),(W2,H4),(255,0,255),2)
    cv.rectangle(image,(W2,H3),(W3,H4),(255,0,255),2)
    cv.rectangle(image,(W3,H3),(W4,H4),(255,0,255),2)
    cv.rectangle(image,(W4,H3),(W5,H4),(255,0,255),2)
    cv.rectangle(image,(W5,H3),(W6,H4),(255,0,255),2)
    cv.rectangle(image,(W6,H3),(W7,H4),(255,0,255),2)
    cv.rectangle(image,(W7,H3),(W8,H4),(255,0,255),2)
    cv.rectangle(image,(W8,H3),(W9,H4),(255,0,255),2)
    cv.rectangle(image,(W9,H3),(W10,H4),(255,0,255),2)
    cv.rectangle(image,(W10,H3),(W11,H4),(255,0,255),2)
    cv.rectangle(image,(W11,H3),(W12,H4),(255,0,255),2)
    cv.rectangle(image,(W12,H3),(W13,H4),(255,0,255),2)
    cv.rectangle(image,(W13,H3),(W14,H4),(255,0,255),2)
    cv.rectangle(image,(W14,H3),(W15,H4),(255,0,255),2)
    cv.rectangle(image,(W15,H3),(W16,H4),(255,0,255),2)
    
    
#333#!识别区
    ID=1
    QR_info=[]
#    cv.rectangle(image,(150,84),(730,168),(255,0,0),2)
    info=[]
#3发情次数 1-12
#    cv.rectangle(image,(W_b_A_2,H3_0),(W_e_A_1,H3_1),(0,255,255),2)
    cv.rectangle(image,(W1,H4),(W2,H5),(155,155,255),2)
    cv.rectangle(image,(W2,H4),(W3,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H4),(W4,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H4),(W5,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H4),(W6,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H4),(W7,H5),(155,155,255),2)    
    cv.rectangle(image,(W7,H4),(W8,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H4),(W9,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H4),(W10,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H4),(W11,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H4),(W12,H5),(155,155,255),2)    
    cv.rectangle(image,(W12,H4),(W13,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H4),(W14,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1    
    cv.rectangle(image,(W14,H4),(W15,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1    
    cv.rectangle(image,(W15,H4),(W16,H5),(155,255,0),2)
    info_array=shengchengshuju(ID,H4,H5,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1

###4二维码、断奶数、断奶窝重、
#    4.1二维码
    cv.rectangle(image,(W1,H5),(W5,H11),(155,255,0),2)
#    info_array=shengchengshuju(ID,H4,H5,W14,W15,image,photoName)
#    QR_info.append(info_array)
#    ID=ID+1    
    cv.rectangle(image,(W5,H5),(W9,H11),(155,255,0),2)
#    info_array=shengchengshuju(ID,H4,H5,W15,W16,image,photoName)
#    QR_info.append(info_array)
#    ID=ID+1
#    标题
    cv.rectangle(image,(W9,H5),(W10,H6),(155,155,255),2)
    cv.rectangle(image,(W10,H5),(W13,H6),(155,155,255),2)

#    4.2断奶数
    cv.rectangle(image,(W9,H6),(W10,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1   
    cv.rectangle(image,(W9,H7),(W10,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W9,H8),(W10,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W9,H9),(W10,H10),(155,255,0),2)
    info_array=shengchengshuju(ID,H9,H10,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W9,H10),(W10,H11),(155,255,0),2)
    info_array=shengchengshuju(ID,H10,H11,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1 
#     4.3.1断奶窝重
    cv.rectangle(image,(W10,H6),(W11,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1   
    cv.rectangle(image,(W10,H7),(W11,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W10,H8),(W11,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W10,H9),(W11,H10),(155,255,0),2)
    info_array=shengchengshuju(ID,H9,H10,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W10,H10),(W11,H11),(155,255,0),2)
    info_array=shengchengshuju(ID,H10,H11,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
#     4.3.2断奶窝重
    cv.rectangle(image,(W11,H6),(W12,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1   
    cv.rectangle(image,(W11,H7),(W12,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W11,H8),(W12,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W11,H9),(W12,H10),(155,255,0),2)
    info_array=shengchengshuju(ID,H9,H10,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1 
#    cv.rectangle(image,(W11,H10),(W12,H11),(155,255,0),2)
#    info_array=shengchengshuju(ID,H10,H11,W11,W12,image,photoName)
#    QR_info.append(info_array)
#    ID=ID+1
#     4.3.3断奶窝重
    cv.rectangle(image,(W12,H6),(W13,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1   
    cv.rectangle(image,(W12,H7),(W13,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W12,H8),(W13,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W12,H9),(W13,H10),(155,255,0),2)
    info_array=shengchengshuju(ID,H9,H10,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1 
    cv.rectangle(image,(W11,H10),(W13,H11),(155,255,0),2)
    info_array=shengchengshuju(ID,H10,H11,W11,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
#5胎次
#    5.1标题
    cv.rectangle(image,(W1,H11),(W2,H12),(155,155,255),2)
    cv.rectangle(image,(W2,H11),(W3,H12),(155,155,255),2)
    cv.rectangle(image,(W3,H11),(W4,H12),(155,155,255),2)
    cv.rectangle(image,(W4,H11),(W5,H12),(155,155,255),2)
    cv.rectangle(image,(W5,H11),(W6,H12),(155,155,255),2)
    cv.rectangle(image,(W6,H11),(W7,H12),(155,155,255),2)
    cv.rectangle(image,(W7,H11),(W8,H12),(155,155,255),2)
    cv.rectangle(image,(W8,H11),(W10,H12),(155,155,255),2)
    cv.rectangle(image,(W10,H11),(W12,H12),(155,155,255),2)
    cv.rectangle(image,(W12,H11),(W13,H12),(155,155,255),2)
#    5.2.1 胎次
    cv.rectangle(image,(W1,H12),(W2,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W1,H13),(W2,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W1,H14),(W2,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W1,H15),(W2,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W1,H16),(W2,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W1,W2,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.2 健仔
    cv.rectangle(image,(W2,H12),(W3,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H13),(W3,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H14),(W3,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H15),(W3,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W2,H16),(W3,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W2,W3,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.3 胎次
    cv.rectangle(image,(W3,H12),(W4,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H13),(W4,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H14),(W4,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H15),(W4,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H16),(W4,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.4 胎次
    cv.rectangle(image,(W4,H12),(W5,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H13),(W5,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H14),(W5,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H15),(W5,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H16),(W5,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.5 胎次
    cv.rectangle(image,(W5,H12),(W6,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H13),(W6,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H14),(W6,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H15),(W6,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H16),(W6,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.6 胎次
    cv.rectangle(image,(W6,H12),(W7,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H13),(W7,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H14),(W7,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H15),(W7,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H16),(W7,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.7 胎次
    cv.rectangle(image,(W7,H12),(W8,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H13),(W8,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H14),(W8,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H15),(W8,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H16),(W8,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.8 胎次
    cv.rectangle(image,(W8,H12),(W9,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H13),(W9,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H14),(W9,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H15),(W9,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H16),(W9,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.2.9 胎次
    cv.rectangle(image,(W9,H12),(W10,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H13),(W10,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H14),(W10,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H15),(W10,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H16),(W10,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    
    
#    5.3.1 乳头数 
    cv.rectangle(image,(W10,H12),(W11,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H13),(W11,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H14),(W11,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H15),(W11,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H16),(W11,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.3.2 乳头数 
    cv.rectangle(image,(W10,H12),(W11,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H13),(W11,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W10,W11,image,photoName)
    QR_info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H14),(W11,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H15),(W11,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H16),(W11,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.3.3 乳头数 
    cv.rectangle(image,(W11,H12),(W12,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H13),(W12,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H14),(W12,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H15),(W12,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H16),(W12,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
#    5.3.4 接产员
    cv.rectangle(image,(W12,H12),(W13,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H13),(W13,H14),(155,255,0),2)
    info_array=shengchengshuju(ID,H13,H14,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H14),(W13,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H15),(W13,H16),(155,255,0),2)
    info_array=shengchengshuju(ID,H15,H16,W12,W13,image,photoName)
    QR_info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H16),(W13,H17),(155,255,0),2)
    info_array=shengchengshuju(ID,H16,H17,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
#6免疫
#    6.1标题
    cv.rectangle(image,(W2,H17),(W3,H18),(155,155,255),2)
    cv.rectangle(image,(W3,H17),(W4,H18),(155,155,255),2)
    cv.rectangle(image,(W4,H17),(W5,H18),(155,155,255),2)
    cv.rectangle(image,(W5,H17),(W6,H18),(155,155,255),2)
    cv.rectangle(image,(W6,H17),(W7,H18),(155,155,255),2)
    cv.rectangle(image,(W7,H17),(W8,H18),(155,155,255),2)
    cv.rectangle(image,(W8,H17),(W9,H18),(155,155,255),2)
    cv.rectangle(image,(W9,H17),(W10,H18),(155,155,255),2)
    cv.rectangle(image,(W10,H17),(W11,H18),(155,155,255),2)
    cv.rectangle(image,(W11,H17),(W12,H18),(155,155,255),2)
    cv.rectangle(image,(W12,H17),(W13,H18),(155,155,255),2)
    
    
#    6.1.0
    cv.rectangle(image,(W3,H18),(W4,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H19),(W4,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W3,H20),(W4,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W3,W4,image,photoName)
    info.append(info_array)
    ID=ID+1
    
#    6.1.1
    cv.rectangle(image,(W4,H18),(W5,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H19),(W5,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W4,W5,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W4,H20),(W5,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W4,W5,image,photoName)
    QR_info.append(info_array)
    ID=ID+1
#    6.1.2
    cv.rectangle(image,(W5,H18),(W6,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H19),(W6,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W5,W6,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W5,H20),(W6,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W5,W6,image,photoName)
    QR_info.append(info_array)
    ID=ID+1
#    6.1.3
    cv.rectangle(image,(W6,H18),(W7,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H19),(W7,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W6,W7,image,photoName)
    QR_info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W6,H20),(W7,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W6,W7,image,photoName)
    info.append(info_array)
    ID=ID+1
#    6.1.4
    cv.rectangle(image,(W7,H18),(W8,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H19),(W8,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W7,H20),(W8,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W7,W8,image,photoName)
    info.append(info_array)
    ID=ID+1
#    6.1.5
    cv.rectangle(image,(W8,H18),(W9,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H19),(W9,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W8,H20),(W9,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W8,W9,image,photoName)
    info.append(info_array)
    ID=ID+1
#    6.1.6
    cv.rectangle(image,(W9,H18),(W10,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H19),(W10,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W9,H20),(W10,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W9,W10,image,photoName)
    info.append(info_array)
    ID=ID+1
#    6.1.7
    cv.rectangle(image,(W10,H18),(W11,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H19),(W11,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W10,H20),(W11,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W10,W11,image,photoName)
    info.append(info_array)
    ID=ID+1
#    6.1.8
    cv.rectangle(image,(W11,H18),(W12,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H19),(W12,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W11,H20),(W12,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W11,W12,image,photoName)
    info.append(info_array)
    ID=ID+1
#    6.1.9
    cv.rectangle(image,(W12,H18),(W13,H19),(155,255,0),2)
    info_array=shengchengshuju(ID,H18,H19,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H19),(W13,H20),(155,255,0),2)
    info_array=shengchengshuju(ID,H19,H20,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W12,H20),(W13,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W12,W13,image,photoName)
    info.append(info_array)
    ID=ID+1

#7背标测量、背标值、妊娠中断
#    标题
    cv.rectangle(image,(W13,H5),(W16,H6),(155,155,255),2)
    cv.rectangle(image,(W13,H9),(W16,H10),(155,155,255),2)
    cv.rectangle(image,(W13,H13),(W16,H14),(155,155,255),2)
#7.1
    cv.rectangle(image,(W13,H6),(W14,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H7),(W14,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H8),(W14,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    
    cv.rectangle(image,(W14,H6),(W15,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H7),(W15,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H8),(W15,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    
    cv.rectangle(image,(W15,H6),(W16,H7),(155,255,0),2)
    info_array=shengchengshuju(ID,H6,H7,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H7),(W16,H8),(155,255,0),2)
    info_array=shengchengshuju(ID,H7,H8,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H8),(W16,H9),(155,255,0),2)
    info_array=shengchengshuju(ID,H8,H9,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
#7.2
    cv.rectangle(image,(W13,H10),(W14,H11),(155,255,0),2)
    info_array=shengchengshuju(ID,H10,H11,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H11),(W14,H12),(155,255,0),2)
    info_array=shengchengshuju(ID,H11,H12,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W13,H12),(W14,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    
    cv.rectangle(image,(W14,H10),(W15,H11),(155,255,0),2)
    info_array=shengchengshuju(ID,H10,H11,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H11),(W15,H12),(155,255,0),2)
    info_array=shengchengshuju(ID,H11,H12,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H12),(W15,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    
    cv.rectangle(image,(W15,H10),(W16,H11),(155,255,0),2)
    info_array=shengchengshuju(ID,H10,H11,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H11),(W16,H12),(155,255,0),2)
    info_array=shengchengshuju(ID,H11,H12,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H12),(W16,H13),(155,255,0),2)
    info_array=shengchengshuju(ID,H12,H13,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
#7.3
    cv.rectangle(image,(W13,H14),(W14,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W13,W14,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W14,H14),(W15,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W14,W15,image,photoName)
    info.append(info_array)
    ID=ID+1
    cv.rectangle(image,(W15,H14),(W16,H15),(155,255,0),2)
    info_array=shengchengshuju(ID,H14,H15,W15,W16,image,photoName)
    info.append(info_array)
    ID=ID+1
    
    
#    **校验位
    cv.rectangle(image,(W15,H20),(W16,H21),(155,255,0),2)
    info_array=shengchengshuju(ID,H20,H21,W15,W16,image,photoName)
#8书写数据日期
    cv.rectangle(image,(W_b_A_2,H21),(W_e_A_1,H22),(0,255,255),2)
    cv.rectangle(image,(W1,H21),(W4,H22),(255,0,255),2)
    cv.rectangle(image,(W4,H21),(W9,H22),(255,0,255),2)
    cv.rectangle(image,(W9,H21),(W12,H22),(255,0,255),2)
    cv.rectangle(image,(W12,H21),(W16,H22),(255,0,255),2)

    cv.rectangle(image,(W_b_A_2,H22),(W_e_A_1,H23),(0,255,255),2)
    cv.rectangle(image,(W1,H22),(W16,H23),(255,0,255),2)
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
            print('返回值',b)
            Sum=Sum+x
        print('识别成功的张数',Sum)
        
#                Orig_url = filepath+filename
#                url.append(Orig_url)
#        #        print(Orig_url)
#                photoName=Orig_url.split("/")[-1]
##                name.append(photoName)
#        print('照片总张数',len(name))# 