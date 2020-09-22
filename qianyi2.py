import os
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import keras
from keras.models import Model
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.utils import np_utils
from keras.applications.resnet50 import ResNet50

#1获取数据标签
def tranverse_images(path):
    labels = pd.DataFrame()
    first_dir_file = [file for file in os.listdir(path)]
    for item in first_dir_file:
        flower = [image for image in os.listdir(path+item)]
        labels_data = pd.DataFrame({'flower': flower, 'labels': item})
        labels = pd.concat((labels, labels_data))
    return labels
    

    

#img = cv2.imread('./data2/nosmoke/bl_nosmoke_100.jpg')
#img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.imshow(img1)
#print(img.shape)
#img_2 = cv2.resize(img, (224, 224))
#print(img_2.shape)
#img_1 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
#plt.imshow(img_1)
#批量缩放
def resize_image(path1):
    images = [img for img in os.listdir(path1)]
    print(images)
    total = 0
    start_time = time.time()
    for img in images:
        path=path1 + img
        fileList = os.listdir(path)
        list_name=0
        for fileName in fileList: 
            img_path_name=path+'/'+fileName
#            print(img_path_name)
            label=img_path_name.split('/')[-2]
            list_name=list_name+1
            img_path_newname=path+'/'+label+''+(str(list_name))+'.jpg'
            print(img_path_newname)
#            print(img_path_name)
            img = cv2.imread(img_path_name)
#            print(img)
            img1=cv2.resize(img, (224, 224))
            print(img1)
            if(str(img1)=='None'):
                print('error')
##            img1 = cv.resize(img, (100,100))
#            
            else:
                print('ok')
#            total += 1
                os.remove(img_path_name)
                cv2.imwrite(img_path_newname, img1)
#
    print('all images are resized, all resized image is {}.'.format(total))
    end_time = time.time()
    print('Time is {}.'.format(end_time - start_time))

# image to array
def image2array(labels, path):
    lst_imgs = [l for l in labels['flower']]
    p=[j for j in labels['labels']]
    print(lst_imgs)
    print(p)
#    return np.array([np.array(Image.open(path+img)) for img in lst_imgs])


if __name__ == '__main__':
#1获取数据标签
#    切割图片4等分
    labels = tranverse_images('./data2/')
    #t=labels.head()
    print(labels)
#2    重新定义尺寸
#    resize_image(path1='./data2/')
    X = image2array(labels, './data2/')
#    print(X.shape)
#    np.save('./X_train.npy', X)
