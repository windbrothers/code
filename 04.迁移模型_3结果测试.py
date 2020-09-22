# -*- coding: utf-8 -*-
"""
读取使用自训练模型进行测试
"""
from skimage import transform,io
from keras import applications
# 要载入模型，需要导入此函数
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from skimage import transform,io
import os
def readImage(path_dir=r'Data-测试'):
    imgs=[]
    labels=[]
    for (root, dirs, files) in os.walk(path_dir):
        if files:
            for f in files:
                path = os.path.join(root,f)
                img=io.imread(path)
                dst=transform.resize(img, (50, 50))
                imgs.append(dst)
                labels.append(path)
    return np.array(imgs),labels
#加载模型
print('load model')
#models=["VGG16","VGG19","InceptionV3","ResNet50"]
model1 = applications.ResNet50(include_top=False, weights='imagenet')
model2 = load_model('model.h5')
#读取图像并5张
#model1.summary()
imageArr,labels=readImage()
print(imageArr.shape)
freatueMap=model1.predict(imageArr)
inputShape=1
for i in range(1,len(freatueMap.shape),1):
    inputShape*=freatueMap.shape[i]
freatueMap=freatueMap.reshape(-1,inputShape)
result=model2.predict(freatueMap)
print(result.shape)
result=np.argmax(result,axis=1)
print(result.shape)

label =np.load('./features/label.npy',allow_pickle=True)
label=eval(str(label))
print(label)

for i,srcDir in zip(result,labels):
    tag='有烟'
    if i==1:
        tag='无烟'
    print(tag,srcDir)