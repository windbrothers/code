# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:00:35 2020

@author: zhyf
E-mail:zhyfwcy@gmail.com

说明：

"""
import cv2 as cv
import numpy as np
def shengchengshuju(ID,y0,y1,x0,x1,image):
    y0=y0
    y1=y1
    x0=x0
    x1=x1
    ptStart = (x0, y0)
    ptEnd = (x1, y1)
    ptStart1 = (x0, y1)
    ptEnd1 = (x1, y0)
    cropped = image[y0:y1,x0:x1]
    pint_W=cropped.shape[0]
    pint_H=cropped.shape[1]
    area=(pint_W)*(pint_H)
    Wk=0#Wk 白色
    Bk=0#Bk 黑色
    image1 =cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)
    R = image1[:, :, 0]
    R1=cropped[:, :, 0]
    G1=cropped[:, :, 1]
    B1=cropped[:, :, 1]
    R_mean =int(np.mean(R))
#    print('R_mean',R_mean)
    for i in range(pint_W):
        for j in range(pint_H):
            R_pix=R1[i][j]
#            G_pix=G1[i][j]
#            B_pix=B1[i][j]
            if(R_pix>R_mean):
                cropped[i][j] = [0, 0, 0]
#            elif(R_pix<80 and G_pix<80 and B_pix<80 ):
#                cropped[i][j] = [0, 0, 0]
            else:
                cropped[i][j] = [255, 0, 0]                
#            G_pix=G1[i][j]
#            B_pix=B1[i][j]
            D_B=cropped[i][j]
#            if(G_pix==0 and B_pix==0 ):

            if(D_B[0]==255 ):
                    Bk=Bk+1
            else:
                    Wk=Wk+1
    R=Bk/area
    
    if(R>0.6):
        print(R,Bk,Wk,area)
#    R=1
    if(R>0.65):
#        print(R,Bk,Wk,area)
#        cv.line(image, ptStart, ptEnd, (255, 180, 0), 1, 4)
#        cv.line(image, ptStart1, ptEnd1, (255, 180, 0), 1, 4)
#        cv.line(image, ptStart, ptEnd, (0, 255, 0), 1, 4)
#        cv.line(image, ptStart1, ptEnd1, (0, 255, 0), 1, 4)
        sign=1
    else:
        sign=0
    cv.waitKey()
    return sign
