 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:45:44 2019

@author: zhyf


"""

# -*- coding : utf-8 -*-
# Author: Tom Yu
import cv2 
import numpy as np
import time


#img = cv2.imread("img.jpg")
#hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


def nothing(x):
  pass
def createbars():
  """
  实现创建六个滑块的作用，分别控制H、S、V的最高值与最低值
  """
  cv2.createTrackbar("H_l","image",0,180,nothing)
  cv2.createTrackbar("H_h","image",0,180,nothing)
  cv2.createTrackbar("S_l","image",0,255,nothing)
  cv2.createTrackbar("S_h","image",0,255,nothing)
  cv2.createTrackbar("V_l","image",0,255,nothing)
  cv2.createTrackbar("V_h","image",0,255,nothing)
cv2.namedWindow("image")

createbars()#创建六个滑块 


  
lower = np.array([0,153,45])#设置初始值
upper = np.array([180,255,255])
#cap = cv2.VideoCapture( r'C:\Users\Administrator\Desktop\article\data\3.mp4' )
cap = cv2.VideoCapture( r'1.avi' )
#cap = cv2.VideoCapture(0)#获取摄像头图像
while (cap.isOpened()):
  ret,frame = cap.read()
  if ret == False:

      break
  hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#将图片由BGR颜色空间转化成HSV空间，HSV可以更好地分割颜色图形
  lower[0]=cv2.getTrackbarPos("H_l","image")#获取"H_l"滑块的实时值
  upper[0]=cv2.getTrackbarPos("H_h","image")#获取"H_h"滑块的实时值
  lower[1]=cv2.getTrackbarPos("S_l","image")
  upper[1]=cv2.getTrackbarPos("S_h","image")
  lower[2]=cv2.getTrackbarPos("V_l","image")
  upper[2]=cv2.getTrackbarPos("V_h","image")
  
  mask = cv2.inRange(hsv_frame,lower,upper)#cv2.inrange()函数通过设定的最低、最高阈值获得图像的掩膜
  dilation = cv2.dilate(mask,np.ones((1,1),np.uint8),iterations = 1)
  mask = cv2.erode(dilation,np.ones((3,3),np.uint8),iterations = 1)
  dilation = cv2.dilate(mask,np.ones((1,1),np.uint8),iterations = 1)
  mask = cv2.erode(dilation,np.ones((3,3),np.uint8),iterations = 1)
  masked=cv2.add(frame,np.zeros(np.shape(frame),dtype=np.uint8),mask=mask)
  
  cv2.imshow("img",frame)
  cv2.imwrite("img.jpg",frame)
  cv2.imshow("mask",mask)
  cv2.imwrite("mask.jpg",mask)
  cv2.imshow("masked",masked)
  cv2.imwrite("masked.jpg",masked)
  time.sleep(3)
  if cv2.waitKey(40) & 0xFF == ord('c'):
  
    break
cap.release()   
cv2.destroyAllWindows()