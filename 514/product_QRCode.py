# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:03:27 2020

@author: zhyf
E-mail:zhyfwcy@gmail.com

说明：

"""
from PIL import Image
from pyzbar import pyzbar
import cv2  as cv 
import numpy as np
def decode_qr_code(ID,y0,y1,x0,x1,image):
    y0=y0
    y1=y1
    x0=x0
    x1=x1
    cropped = image[y0:y1,x0:x1]
    cropped=cv.resize(cropped,(175,130))
#    Mask = cv.erode(cropped,np.ones((5,5),np.uint8),iterations = 1)
#    cropped = cv.dilate(Mask,np.ones((3,3),np.uint8),iterations = 1)
    results= pyzbar.decode(Image.fromarray(cropped), symbols=[pyzbar.ZBarSymbol.QRCODE])
    if len(results):
        sign=results[0].data.decode("utf-8")
    else:
        sign='ERROR'
    return sign
