# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:39:00 2020

@author: zhyf


"""

 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:45:44 2019

@author: zhyf


"""

# -*- coding : utf-8 -*-
# Author: Tom Yu
import cv2 
import numpy as np
  

#img = cv2.imread("img.jpg")
#hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  
lower = np.array([70,28,105])#设置初始值
upper = np.array([113,110,255])
#cap = cv2.VideoCapture( r'C:\Users\Administrator\Desktop\article\data\1.mp4' )
cap = cv2.VideoCapture( r'C:\Users\Administrator\Desktop\article\data\5.avi' )
#cap = cv2.VideoCapture(0)#获取摄像头图像
while (cap.isOpened()):
  ret,frame = cap.read()
  if ret == False:

      break
  hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#将图片由BGR颜色空间转化成HSV空间，HSV可以更好地分割颜色图形
  mask = cv2.inRange(hsv_frame,lower,upper)#cv2.inrange()函数通过设定的最低、最高阈值获得图像的掩膜
  masked=cv2.add(frame,np.zeros(np.shape(frame),dtype=np.uint8),mask=mask)
  cv2.imshow("img",frame)
#  cv2.imwrite("img.jpg",frame)
  cv2.imshow("smoke_mask",mask)
#  cv2.imwrite("mask.jpg",mask)
  cv2.imshow("smoke",masked)
#  cv2.imwrite("masked.jpg",masked)
  
  if cv2.waitKey(40) & 0xFF == ord('c'):
  
    break
cap.release()   
cv2.destroyAllWindows()