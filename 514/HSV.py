# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:35:16 2020

@author: Administrator
"""

import cv2 as cv 
import os
from PIL import Image
import numpy as np
import time
def hsv(img):
    YCrCb_img=cv.cvtColor(img,cv.COLOR_RGB2YCrCb)
    hsv_img=cv.cvtColor(YCrCb_img,cv.COLOR_BGR2HSV)
#    hsv_img=cv.cvtColor(img,cv.COLOR_RGBA2YUV_I420   )
    
    low_hsv = np.array([0,153,35])
    high_hsv = np.array([180,255,255])
 
    binary=cv.inRange(hsv_img,low_hsv,high_hsv)
#    ret,binary = cv.threshold(hsv_img, 127, 255, 0)
    return hsv_img,binary
def YUV(img):
#    hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsv_img=cv.cvtColor(img,cv.COLOR_RGBA2YUV_I420)
    return hsv_img
def YCrCb(img):
#    hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsv_img=cv.cvtColor(img,cv.COLOR_RGB2YCrCb)
    hsv_img=img[:,:,2]
    return hsv_img
def HLS(img):
    hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    
    hsv_img=cv.cvtColor(img,cv.COLOR_BAYER_GR2BGRA)
    return hsv_img
def RGB(img):

    print(img.shape)

    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]
    R_mean =int( np.mean(R))
    print(R_mean)#   
    print(B)
    print(">>>>>>>>>>>>>")

        
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
           
            pix=B[i][j]
            print(pix)
            if(pix>R_mean):           
                img[i][j] = [0, 0, 0]
#            time.sleep(1)
#]

#    print(img)



    return img
def contrast_brightness_demo(image, c, b):  #其中c为对比度，b为每个像素加上的值（调节亮度）
    blank = np.zeros(image.shape, image.dtype)   #创建一张与原图像大小及通道数都相同的黑色图像
    dst = cv.addWeighted(image, c, blank, 1-c, b) #c为加权值，b为每个像素所加的像素值
    ret, dst = cv.threshold(dst, 25, 255, cv.THRESH_BINARY)
    return dst

if __name__ == '__main__':
    path='./test1'
    hsv_img_path='./dhsv/'
    binary_img_path='./binary/'
    zzz=1
    for filename in os.listdir(path):
#        print('处理照片张数是：',zzz)        
        image_path = path+'/'+filename
        portion = os.path.split(image_path)
        image = Image.open(image_path)
        img = cv.imread(image_path)
        name=portion[1]
        hsv_img,binary=hsv(img)
#        hsv_img=YUV(img)
#        hsv_img=YCrCb(img)
#        hsv_img= RGB(img)
#        print(name)

        hsv_img_save=hsv_img_path+name
        cv.imwrite(hsv_img_save,hsv_img)
#        binary_img_save=binary_img_path+name
#        cv.imwrite(binary_img_save,binary)
        zzz=zzz+1

