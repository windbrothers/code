# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:07:38 2020

@author: Administrator
"""
import os 
import cv2
import numpy as np
def hsv(path,filename):
    img = cv2.imread(path)
    # remove blue color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#    cv2.imwrite(filename[:-5]+'_hsv.jpg', hsv)

    lower_hsv = np.array([156, 43, 46])
    upper_hsv = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lowerb = lower_hsv, upperb = upper_hsv)
#    cv2.imwrite(filename[:-5]+'_mask.jpg', mask)

    lower_hsv2 = np.array([0, 43, 46])
    upper_hsv2 = np.array([10, 255, 255])

    mask2 = cv2.inRange(hsv, lowerb = lower_hsv2, upperb = upper_hsv2)
#    cv2.imwrite(filename[:-5]+'_mask2.jpg', mask2)

    mask3 = mask+mask2
#    print(mask3)1
    Mean=np.mean(mask3)
    print(Mean)
    if(Mean<157):
        cv2.imwrite('./0/'+filename+'_mask3.jpg', img)
#    cv2.imwrite(filename[:-5]+'_mask3.jpg', mask3)
    else:
        cv2.imwrite('./1/'+filename+'_mask3.jpg', img)
    return 'ok'

if __name__ == '__main__':

    Sum =0
    filepath='./cut1/'
    k=0
    for filename in os.listdir(filepath):
            print('正在执行的次数：',k)
            path = filepath+filename
            result=hsv(path,filename)
            print(result)
            k=k+1
