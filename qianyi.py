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

#提取标签
def tranverse_images(path):
    labels = pd.DataFrame()
    first_dir_file = [file for file in os.listdir(path)]
#    print(first_dir_file)
    for item in first_dir_file:
#        print(item)
        flower = [image for image in os.listdir(path+item)]
        labels_data = pd.DataFrame({'photos_name': flower, 'labels': item})
        labels = pd.concat((labels, labels_data))
    return labels
        
labels = tranverse_images('./flower_photos/')
print(labels)
        
# resize
def resize_image(path1,path2):
    images = [img for img in os.listdir(path1)]

#    print(images)
    total = 0
#    start_time = time.time()
    for img in images:
        path=path1 + img
#        print(path)
#        print(fileList)
        fileList = os.listdir(path)
        for fileName in fileList: 
#            print(fileName)
            img_path_name=path+'/'+fileName
#            print(path)
#            print(img_path_name)
            img = cv2.imread(img_path_name)
            img = cv2.resize(img, (224, 224))
            total += 1
#            print('now is resizing {} image.'.format(total))
            cv2.imwrite(path2+fileName, img)
#            cv2.imwrite(path+'/new'+str(total)+'.jpg', img)
#    print('all images are resized, all resized image is {}.'.format(total))
#    end_time = time.time()
#    print('the resize time is {}.'.format(end_time - start_time))
#        
resize_image(path1='./flower_photos/',path2='./resize_flower_photos/')

# image to array
def image2array(labels, path):
    print("以下结果")
    
    lst_imgs = [l for l in labels['photos_name']]
#    print(lst_imgs)
    return np.array([np.array(Image.open(path+img)) for img in lst_imgs])
    
X = image2array(labels, './resize_flower_photos/')
#print('X   ededed',X)
#print(X.shape)
np.save('./X_train.npy', X)
lbl = LabelEncoder().fit(list(labels['labels'].values))
#print(labels)
labels['code_labels'] = pd.DataFrame(lbl.transform(list(labels['labels'].values)))

y=labels['code_labels']
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)


X_train = np.array(X_train,'float32')
X_test = np.array(X_test,'float32')
#
X_train /=255
X_test /= 255
y_train = np_utils.to_categorical(y_train, 2)
y_test = np_utils.to_categorical(y_test, 2)



def flower_model(X_train, y_train):
    base_model = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    for layers in base_model.layers:
        layers.trainable = False
    
        model = Flatten()(base_model.output)
        model = Dense(128, activation='relu')(model)
        model = Dropout(0.5)(model)
        model = Dense(2, activation='softmax')(model)
        
        model = Model(inputs=base_model.input, outputs=model)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X_train, y_train, batch_size=128, epochs=5)
    
    return model
model = flower_model(X_train, y_train)
model.evaluate(X_test, y_test, verbose=0)