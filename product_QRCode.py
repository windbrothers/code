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

def decode_qr_code(ID,y0,y1,x0,x1,image):
    y0=y0
    y1=y1
    x0=x0
    x1=x1
    Mask = image[y0:y1,x0:x1]
    Mask=cv.resize(Mask,(175,130))
    results= pyzbar.decode(Image.fromarray(Mask), symbols=[pyzbar.ZBarSymbol.QRCODE])
    if len(results):
        sign=results[0].data.decode("utf-8")
    else:
        Mask=cv.resize(Mask,(350,260))
        results= pyzbar.decode(Image.fromarray(Mask), symbols=[pyzbar.ZBarSymbol.QRCODE])
        if len(results):
            sign=results[0].data.decode("utf-8")

        else:
            Mask=cv.resize(Mask,(700,520))
            results= pyzbar.decode(Image.fromarray(Mask), symbols=[pyzbar.ZBarSymbol.QRCODE])
            if len(results):
                sign=results[0].data.decode("utf-8")

            else:
                Mask=cv.resize(Mask,(1050,780))
                results= pyzbar.decode(Image.fromarray(Mask), symbols=[pyzbar.ZBarSymbol.QRCODE])
                if len(results):
                    sign=results[0].data.decode("utf-8")

                else:
                    sign='ERROR'

    return sign
