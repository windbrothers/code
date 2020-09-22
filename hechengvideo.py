# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:31:22 2020

@author: Administrator
"""

import cv2 as cv
import os
fps=1
size=(1200,900)
fourecc= cv.VideoWriter_fourcc(*'XVID')
videoWriter =cv.VideoWriter('./1.avi',fourecc,fps,size)
 
filepath='./1/'
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
    
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
    
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
for filename in os.listdir(filepath):
    path = filepath+filename
    frame= cv.imread(path)
    videoWriter.write(frame)
videoWriter.release()
print('ok')