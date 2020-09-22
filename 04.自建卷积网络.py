# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:35:40 2019

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/

conda config --set show_channel_urls yes
"""
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""#使用CPU
os.environ['KERAS_BACKEND'] ='tensorflow'#'theano'# 
from keras.models import Sequential,load_model
from keras.layers import Dense,Dropout,Flatten
from keras.layers.pooling import GlobalAveragePooling2D
from keras import optimizers
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D

from keras.preprocessing.image import ImageDataGenerator
batch_size=64
datagen = ImageDataGenerator(rescale=1.0 / 255)
in_size=(100,100)
bpath='data'

Train=True#False#
if Train:
    input_shape=(*in_size,1)
    base_num=4
    model = Sequential()
    model.add(Conv2D(base_num, (3, 3), input_shape=input_shape, padding='same', activation='tanh'))
    model.add(Conv2D(base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(2*base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(Conv2D(2*base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(4*base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(4*base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(8*base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(8*base_num, (3, 3),  padding='same', activation='tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)));model.add(Flatten())
    #model.add(GlobalAveragePooling2D())
    model.add(Dense(80, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))#tf.nn.log_softmax
    
    lrate = 0.01;decay = 0.007;momentum=0.3
    
    optimizer = optimizers.SGD(lr=lrate, momentum=momentum, decay=decay, nesterov=False)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
    model.summary()#显示模型
    #import sys;sys.exit();
    
    train = datagen.flow_from_directory('%s-训练'%bpath,target_size=in_size,color_mode='grayscale',batch_size=batch_size,class_mode='categorical',shuffle=False)
        
    
    
    from keras.callbacks import ModelCheckpoint,EarlyStopping,History
    history = History()
    
    model_checkpoint = ModelCheckpoint('model-cnn.hdf5', monitor='loss', save_best_only=True)
    EarlyStopping=EarlyStopping(monitor='acc', patience=25, verbose=2, mode='auto')
    callbacks = [
                history,
                model_checkpoint,
                EarlyStopping
            ]
    
    valid = datagen.flow_from_directory('%s-验证'%bpath,target_size=in_size,color_mode='grayscale',batch_size=batch_size,class_mode='categorical',shuffle=False) 
    
    
    model.fit_generator(train,steps_per_epoch=len(train.classes)/train.batch_size,
            epochs=200,
            validation_data=valid,
                  callbacks=callbacks,
            validation_steps=len(valid.classes)/valid.batch_size,
            verbose=2)
else:
    model=load_model('model-cnn.hdf5')
    model.summary()
from keras.utils import np_utils
from sklearn import metrics
import numpy as np
import time
t0=time.time()
test = datagen.flow_from_directory('%s-测试'%bpath,target_size=in_size,color_mode='grayscale',batch_size=batch_size,class_mode='categorical',shuffle=False)
y_pred_=model.predict_generator(test, len(test.classes)/test.batch_size)
t1=time.time()-t0
t=t1/y_pred_.shape[0]*100
print('100个样本耗时：',t)
test_labels=np_utils.to_categorical(test.classes)
y_true=test_labels.argmax(axis=1)
y_pred=y_pred_.argmax(axis=1)
print(y_true.shape,y_pred.shape)
#print(y_true,y_pred)
uniques = np.unique(y_true,axis=0)
print(uniques.shape, uniques)
classify_report = metrics.classification_report(y_true, y_pred)

confusion_matrix = metrics.confusion_matrix(y_true, y_pred)
overall_accuracy = metrics.accuracy_score(y_true, y_pred)
acc_for_each_class = metrics.precision_score(y_true, y_pred, average=None)
average_accuracy = np.mean(acc_for_each_class)
score = metrics.accuracy_score(y_true, y_pred)
print('classify_report : \n', classify_report)
print('confusion_matrix : \n', confusion_matrix)
import pandas as pd
data1 = pd.DataFrame(confusion_matrix)
data1.to_csv('confusion_matrix.csv')

print('acc_for_each_class : \n', acc_for_each_class)
print('average_accuracy: {0:f}'.format(average_accuracy))
print('overall_accuracy: {0:f}'.format(overall_accuracy))
print('score: {0:f}'.format(score))
acc_for_each_class=np.around(acc_for_each_class, decimals=2)
np.savetxt('afec_mycnn.csv',acc_for_each_class)
