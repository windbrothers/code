import os
import cv2
import numpy as np

ROI = ((0, 0), (1200, 900))
# tmp_roi = ((267, 1255), (304, 1294))

def red_detection(filename):
    print(filename)

    img = cv2.imread(filename)

    # crop ROI
    img = img[ROI[0][1]:ROI[1][1], ROI[0][0]:ROI[1][0]]

    # remove blue color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite(filename[:-5]+'_hsv.jpg', hsv)

    lower_hsv = np.array([156, 43, 46])
    upper_hsv = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lowerb = lower_hsv, upperb = upper_hsv)
    cv2.imwrite(filename[:-5]+'_mask.jpg', mask)

    lower_hsv2 = np.array([0, 43, 46])
    upper_hsv2 = np.array([10, 255, 255])

    mask2 = cv2.inRange(hsv, lowerb = lower_hsv2, upperb = upper_hsv2)
    cv2.imwrite(filename[:-5]+'_mask2.jpg', mask2)

    mask3 = mask+mask2
    cv2.imwrite(filename[:-5]+'_mask3.jpg', mask3)


#filename = 'images/52张照片/AWXGW191114025_1_5J0135DPAJ1272A_1591233321.jpeg'
#red_detection(filename)

#exit(0)

#dirname = 'images/52张照片/'
dirname = 'images/badcase/'
filenames = os.listdir(dirname)
for filename in filenames:
    if filename.endswith('.jpeg'):
        filename = os.path.join(dirname, filename)
        red_detection(filename)
