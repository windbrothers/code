# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:00:35 2020

@author: zhyf
E-mail:zhyfwcy@gmail.com

说明：

"""
import cv2 as cv
#import numpy as np
from color_Model import Color as Color_R
def shengchengshuju(ID,y0,y1,x0,x1,image):
    K=3
    e=y0
    r=y1
    q=x0
    w=x1
    X_L=int((abs(x0-x1)/2)/K)
    Y_L=int((abs(y0-y1)/2)/K)
    center_point_x=int(abs(x0+x1)/2)
    center_point_y=int(abs(y0+y1)/2)
    y0=int(center_point_y-Y_L)
    y1=int(center_point_y+Y_L)
    x0=int(center_point_x-X_L)
    x1=int(center_point_x+X_L)
#    ptStart = (x0, y0)
#    ptEnd = (x1, y1)
#    ptStart1 = (x0, y1)
#    ptEnd1 = (x1, y0)
    cropped = image[y0:y1,x0:x1]
    cropped=cv.resize(cropped,(400,300))
#    path='./R_croped/'
    save_path='./R_croped/Cropped.jpg'
    cv.imwrite(save_path,cropped)
#    print(cropped)
    hh=Color_R.color_API(save_path)
    print('hhd的结果',hh)
    R='X'
    

    
    ptStart = (q, e)
    ptEnd = (w, r)
    ptStart1 = (q, r)
    ptEnd1 = (w, e)
    
    if(R==0):
        cv.line(image, ptStart, ptEnd, (255, 255, 0), 1, 4)
        cv.line(image, ptStart1, ptEnd1, (255, 255, 0), 1, 4)
        sign=1
    else:
        print('error')
        sign=0
    cv.waitKey()
    return sign
